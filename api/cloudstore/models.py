import os
from typing import List
from django.conf import settings
from django.db import models
from dropbox.dropbox import Dropbox as DropboxService
from dropbox.files import FileMetadata, FolderMetadata

def create_media_dir():
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

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
