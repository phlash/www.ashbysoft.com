#! /usr/bin/env python3
# Push content to Azure storage for production hosting :)
# Author: Phlash

import os, datetime, mimetypes
from dotenv import load_dotenv
from azure.storage.blob import BlockBlobService, ContentSettings

container = '$web'
publish = 'publish'
# CDN expiry, 10mins
max_age = '600'
mimetypes.add_type('audio/ogg', '.ogg')
mimetypes.add_type('application/x-yaml', '.yaml')
mimetypes.add_type('application/x-yaml', '.yml')

# Settings/secrets are in .env file - pull 'em into environment vars
load_dotenv()

# connect to Azure storage
blob_client = BlockBlobService(account_name=os.getenv('AZURE_STORAGE_ACCOUNT'), account_key=os.getenv('AZURE_STORAGE_KEY'))

# iterate (and remember) blobs in '$web' container
blist = {}
for blob in blob_client.list_blobs(container):
    blist[blob.name] = blob

# iterate (and upload) contents of $publish folder, if more recent than blob
for root, subs, files in os.walk('publish'):
    fld = root[len(publish)+1:]
    if len(fld) > 0:
        fld = fld+'/'
    for fil in files:
        lcl = root+'/'+fil
        blb = fld+fil
        ext = os.path.splitext(fil)[1]
        typ = 'application/octet-stream'
        if ext in mimetypes.types_map:
            typ = mimetypes.types_map[ext]
        lst = None
        if blb in blist:
            lst = blist[blb].properties.last_modified
            blist.pop(blb, None)
            tim = datetime.datetime.fromtimestamp(os.path.getmtime(lcl), datetime.timezone.utc)
            if tim < lst:
                continue
        print('uploading: ' + lcl + ' => ' + blb + ' (' + typ + ')')
        age = 'max-age=' + max_age
        cnt = ContentSettings(content_type=typ, cache_control=age)
        blob_client.create_blob_from_path(container, blb, lcl, content_settings=cnt)

# remove unreferenced blobs
for blob in blist:
    print('removing: ' + blob)
    blob_client.delete_blob(container, blob)
