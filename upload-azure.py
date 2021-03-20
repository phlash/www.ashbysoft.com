#! /usr/bin/env python3
# Push content to Azure storage for production hosting :)
# Author: Phlash

import os, datetime, mimetypes, hashlib, base64
from dotenv import load_dotenv
from azure.storage.blob import BlockBlobService, ContentSettings

container = '$web'
publish = 'publish'
# CDN expiry, 10mins
max_age = '600'
mimetypes.add_type('audio/ogg', '.ogg')
mimetypes.add_type('application/x-yaml', '.yaml')
mimetypes.add_type('application/x-yaml', '.yml')

# MD5 a file
def gethash(path):
    with open(path,'rb') as f:
        md5 = hashlib.md5()
        while True:
            d = f.read(8192)
            if not d:
                break
            md5.update(d)
        return md5.digest()

# Settings/secrets are in .env file - pull 'em into environment vars
load_dotenv()

# connect to Azure storage
blob_client = BlockBlobService(account_name=os.getenv('AZURE_STORAGE_ACCOUNT'), account_key=os.getenv('AZURE_STORAGE_KEY'))

# iterate (and remember) blobs in '$web' container
blist = {}
for blob in blob_client.list_blobs(container):
    blist[blob.name] = blob

# iterate (and upload) contents of $publish folder, if more recent than blob and md5 differs
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
            tim = datetime.datetime.fromtimestamp(os.path.getmtime(lcl), datetime.timezone.utc)
            if tim < lst:
                blist.pop(blb, None)
                continue
            hsh = base64.b64encode(gethash(lcl)).decode('utf-8')
            md5 = blist[blb].properties.content_settings.content_md5
            if hsh == md5:
                blist.pop(blb, None)
                continue
            msg='would push('+blb+'):last_modified='+str(lst)+',local_timestamp='+str(tim)+',md5='+md5+',hash='+hsh
            blist.pop(blb, None)
        else:
            msg='would push('+blb+'):missing'
        if os.getenv('NO_UPLOAD'):
            print(msg)
            continue
        print('uploading: ' + lcl + ' => ' + blb + ' (' + typ + ')')
        age = 'max-age=' + max_age
        cnt = ContentSettings(content_type=typ, cache_control=age)
        blob_client.create_blob_from_path(container, blb, lcl, content_settings=cnt)

# remove unreferenced blobs
for blob in blist:
    print('removing: ' + blob)
    blob_client.delete_blob(container, blob)
