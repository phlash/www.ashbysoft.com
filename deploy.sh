#! /bin/sh

# Pull latest
git pull

# Build for local server
/usr/local/bin/hugo

# Build for publication
/usr/local/bin/hugo -b https://ashbysoftstatic.z33.web.core.windows.net/ -d publish

# Push to Azure
./upload-azure.py
