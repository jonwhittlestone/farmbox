import dropbox
import random
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.conf import settings
from cloudstore.models import DropboxApp

def restore_db(request):
    '''
        Restores the SQLite backup
        from Dropbox.
    '''
    try:
        d = DropboxApp()
        d.restore_db()
        messages.add_message(request,
            messages.SUCCESS, 'The database backup has been restored.')
    except Exception as e:
        print(e)
        messages.add_message(request,
            messages.WARNING, f"There was an error restoring the database backup.\n{e}")

    url = reverse('admin:index')
    return redirect(url)


def dropbox_example(request):
    dbx = dropbox.Dropbox(settings.FARMBOX_DROPBOX_ACCESS_TOKEN)

    for entry in dbx.files_list_folder('').entries:
        path = entry.path_lower
        metadata, res = dbx.files_download(path=path)
        out=open(f'dropbox_downloaded_order-{random.randint(0,100)}.xlsx','wb')
        out.write(res.content)
        out.close()


    return HttpResponse('Dropbox Example')
