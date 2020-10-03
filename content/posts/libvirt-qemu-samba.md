---
title: Libvirt, QEMU & Samba
summary: Finally getting a working user-mode shared folder!
date: 2020-10-01T16:05:00.000Z
author: Phlash
---

## Trying to be different again?

Well, yes. I have used many virtualisation systems over the years, and many of them 'just work', especially
well supported tools such as HyperV or VirtualBox, however I wanted to find a solution that was possible
in plain Debian stable, no special repositories (eg: Oracle for VBox), no special agents in the guest (again
VBox needs this) and fully open source (ruling out VMware and HyperV stuff).

Out-of-the-box virt-manager+libvirt+qemu (also kvm for x86 guests) works quite well for actually running my
guest VMs, the networking is well integrated, the GUI (Spice or VNC) is usable too. Choosing qemu as the
virtualiser means many target platforms (eg: ARM, x86, Sparc, ...) and it tends to be first with new targets
too.

The problem I wanted to solve has been around for years, but there hasn't been a single documented solution:
getting a shared folder exposed from my Debian/linux host to a Windows (7) guest VM, while running everything
in user-mode, ie: as me. No special privileges or VMs escaping as root!

### So what *should* work?

There are guides, oh so many guides to ramming special software into the guest so it can talk Plan9, which
is the only qemu built-in protocol for file system access. This is usually a litany of pain and hideously
slow, probably worth avoiding.

What about good old SMB/Samba then? Windows will be fine, just need to install a file server on your host
machine and pipe that networking through.. again, many tutorials, that assume you are running stuff as
root (default libvirt setup), that your VM will have networking (what if you are investigating malware?)
and of course lots of manual messing with smb.conf and trying not to expose your host file system to
elsewhere! It's still slow :(

Interestingly, qemu has built-in pseudo-support for SMB, the -netdev user,smb=/path/to/folder option, as
long as you have Samba installed (doesn't need to be running, qemu does that, plus configuration). This
looks promising, but sadly libvirt and virt-manager know nothing about it so I put this aside for a bit..

I found a 'modern' alternative, the aptly named [Virtio-FS](https://virtio-fs.gitlab.io/), which promises
performance and security, doesn't need network adapters in the guest and support from RedHat - could be
good?

### Virtio-FS

I went with modernity, it has to be better than what it's trying to replace right?

Turns out, it's a little too modern for Debian stable, I needed a backport build of qemu (v5.0+) to get
the necessary support, then of course libvirt/virt-manager know nothing about it, and there isn't a
backport for these - cue much hacking trying to write that supporting logic in bash in a wrapper script
around qemu (don't do this people!)...

Then there's the assumption in the source for virtiofsd (the actual file i/o daemon) that it will be
running as root, because that's how libvirt operates... nope :( I actually went as far as to pull the source
and fix it, but then finally fell foul of a gap in support on the guest - virtio-fs is only supported
on Windows 8+ Gah! I did learn a lot about libvirt/virt-manager and qemu however!

### Samba (again - but working)

So back to option #2, SMB/Samba, using the qemu built-in forwarding to a local instance of smbd that
it configures correctly, all with just one simple command line option, that I now understand how to
provide through libvirt/virt-manager - it doesn't work... Much debugging/rummaging and swearing later
I find that libvirt makes assumptions about how you want to run qemu, in particular it enables the
security sandbox that stops qemu spawning another program - ie: smbd! With this disabled (undocumented
file location BTW), it finally works.

Alleged documentation for [libvirt security](https://www.libvirt.org/kbase/qemu-passthrough-security.html)

## What actually needs doing then?

OK, here's the full list of things to make user-mode SMB work with libvirt/virt-manager/qemu (+kvm):

 * Install required packages: `# aptitude install virt-manager, qemu, qemu-kvm`
 * Create your VM as desired (or import from elsewhere, VBox in my case)
 * Remove the NIC - you will be putting this back via custom arguments below..
 * Use the magic `virt-xml` tool to add custom qemu arguments as per
   [Stack Overflow](https://unix.stackexchange.com/questions/235414/libvirt-how-to-pass-qemu-command-line-args)
   `% virt-xml $(VM) --edit --confirm --qemu-commandline '-netdev'`
   to add a single arg, then
   `% virsh edit $(VM)`
   to get into your chosen text editor and add the following additional lines below -netdev:
   ```
   <qemu:arg value='user,id=hostnet0,smb=/path/to/shared/folder'/>
   <qemu:arg value='-device'/>
   <qemu:arg value='virtio-net-pci,netdev=hostnet0,id=net0,mac=52:54:00:21:69:da,bus=pci.1,addr=0x0'/>

   ```
   NB: You may want to change my MAC for one of yours :)
 * Create/edit a user-mode qemu.conf in `~/.config/libvirt/qemu.conf` and add this text:
   ```
   # Override defaults for libvirt when running in a user session
   # Turn off the sandbox so we can spawn SMBD..
   seccomp_sandbox=0
   ```

This should be it - fire up your VM, ensure you have virtio network drivers installed (part of the OS
unless you are on Win7 - grab them from
[Fedora Virtio-Win](https://docs.fedoraproject.org/en-US/quick-docs/creating-windows-virtual-machines-using-virtio-drivers/)
if you are) and map that drive:
```
C:\> net use X: \\10.0.2.4\qemu
```

Whoo hoo!
