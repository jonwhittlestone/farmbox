from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import dropbox
import random

def dropbox_example(request):
    dbx = dropbox.Dropbox(settings.FARMBOX_DROPBOX_ACCESS_TOKEN)

    for entry in dbx.files_list_folder('').entries:
        path = entry.path_lower
        metadata, res = dbx.files_download(path=path)
        out=open(f'dropbox_downloaded_order-{random.randint(0,100)}.xlsx','wb')
        out.write(res.content)
        out.close()


    return HttpResponse('Dropbox Example')
