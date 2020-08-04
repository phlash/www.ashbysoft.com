#! /bin/sh

now=`date`
act="$GITHUB_EVENT"
del="$GITHUB_DELIVERY"
echo -n "deploy($act/$del)@$now: "

# Skip unless act==push
[ "$act" != "push" ] && echo "not push" && exit 0

# Pull latest (sadly git pull doesn't have an exit code for 'up to date')
res=`git pull`
[ -z "$FORCE_HUGO" -a "$res" = "Already up to date." ] && echo "up to date" && exit 0

# Build for local server
echo "building"

/usr/local/bin/hugo || exit 1

# Build for publication
/usr/local/bin/hugo -b https://www.ashbysoft.com/ -d publish || exit 1

# Push to Azure (in background - or Github webhook times out)
echo "building(done)@$now"
echo "uploading (in background)"
./upload-azure.py &
exit 0
