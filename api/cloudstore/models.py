import os
from typing import List
from zipfile import ZipFile
from pathlib import PosixPath
from django.utils import timezone
from django.conf import settings
from django.db import models
from dropbox.dropbox import Dropbox as DropboxService
from dropbox.files import FileMetadata, FolderMetadata
from order.models import Order

def create_media_dir():
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

def cloud_fetcher():
    '''Download zip of xlsxs to instance storage.'''
    d = DropboxApp()
    # Download zip
    dest_filename = f'fetched-{timezone.now()}.zip'
    path_to_store_local_zip = os.path.join(settings.MEDIA_ROOT, dest_filename)
    path_of_remote_files = settings.NEW_ORDERS_REMOTE_PATH
    files_meta = d.download_all_as_zip(
        path_to_store_local_zip, path_of_remote_files)
    extracted_dir = os.path.join(
        settings.MEDIA_ROOT, settings.NEW_ORDERS_FOLDER)
    # extract zip
    with ZipFile(path_to_store_local_zip, 'r') as zipObj:
        zipObj.extractall(settings.MEDIA_ROOT)
    return extracted_dir, path_to_store_local_zip, files_meta

def remove_remote_form_after_fetch_success(path):
    d = DropboxApp()
    d.remove(f'/{os.path.join(settings.NEW_ORDERS_FOLDER,os.path.basename(path))}')

def upload_form_to_processed_folder(f:PosixPath, order:Order):
    d = DropboxApp()
    fevent_folder_exists = False
    for c in d.list_contents(f'/{settings.PROCESSED_ORDERS_FOLDER}'):
        if c.name == order.fulfillment_event.remote_folder_name:
            fevent_folder_exists = True
    if not fevent_folder_exists:
        d.svc.files_create_folder_v2(f'/{os.path.join(settings.PROCESSED_ORDERS_FOLDER, order.fulfillment_event.remote_folder_name)}')
    dest_path = f'/{os.path.join(settings.PROCESSED_ORDERS_FOLDER, order.fulfillment_event.remote_folder_name)}'
    d.upload(f, dest_path)


class DropboxApp():
    '''
        File operations for dropbox.
        See:
        https://dropbox-sdk-python.readthedocs.io/en/latest/index.html
    '''

    svc: DropboxService

    def __init__(self):
        '''Create connection and local,remote folders.'''
        self.svc = DropboxService(settings.FARMBOX_DROPBOX_ACCESS_TOKEN)
        create_media_dir()
        self.create_remote_folders()

    def create_remote_folders(self):
        '''Create root subfolders if they don't exist.'''
        subfolder_exists = {}
        for sub in settings.CLOUD_SUBFOLDERS:
            subfolder_exists[sub] = False
            for c in self.list_contents():
                if isinstance(c,FolderMetadata) and c.name == sub:
                    subfolder_exists[sub] = True
        for k,v in subfolder_exists.items():
            if not v:
                self.svc.files_create_folder_v2(f'/{k}')


    def upload(self, src, dest = ''):
        '''Upload bytes to dropbox.'''
        filename = os.path.basename(src)
        dest = f'{dest}/{filename}'
        with open(src, "rb") as f:
            self.svc.files_upload(f.read(), dest, mute = True)

    def list_contents(self, path = ''):
        """Lists folder contents.

            :param str path: If empty, it's the
                            default dropbox app folder.
                            `/processed` is the default app's
                            `processed` subfolder
        """
        return self.svc.files_list_folder(path).entries

    def download_all_as_zip(self, local_path, remote_path) -> List[FileMetadata]:
        '''Downloads all files to instance storage'''
        res = self.svc.files_download_zip_to_file(local_path, remote_path)
        return self.list_contents(remote_path)

    def remove(self, path: str):
        self.svc.files_delete_v2(path)

    def move_to_processed_dir(self, ext_ref, dest_path):
        pass
