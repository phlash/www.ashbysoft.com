#! /bin/sh

now=`date`
echo -n "$now: "
# Pull latest (sadly git pull doesn't have an exit code for 'up to date')
res=`git pull`
[ -z "$FORCE_HUGO" -a "$res" = "Already up to date." ] && exit 0

# Build for local server
/usr/local/bin/hugo

# Build for publication
/usr/local/bin/hugo -b https://www.ashbysoft.com/ -d publish

# Push to Azure
./upload-azure.py
echo $now
