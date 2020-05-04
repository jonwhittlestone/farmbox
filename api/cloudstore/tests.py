import os
import pytest
from django.conf import settings
from django.utils import timezone
from cloudstore.models import DropboxApp
from dropbox.files import FolderMetadata

class TestDropboxFileOperations:
    '''Integration tests.'''

    def test_remote_folders_can_be_created_on_init(self):
        remote_folders = ['new-orders','processed-orders']
        t = DropboxApp()
        contents = t.list_contents()
        subfolders = []
        for c in t.list_contents():
            if isinstance(c,FolderMetadata):
                subfolders.append(c.name)
        assert subfolders == list(settings.CLOUD_SUBFOLDERS)


    def test_i_can_store_a_file_in_the_dropbox(self):
        t = DropboxApp()

        # create test file
        token = f'farmbox_testing_{timezone.now()}'
        filename = f"{token}.txt"
        local_file_path = os.path.join(settings.MEDIA_ROOT, filename)
        with open(local_file_path,'w') as f:
            f.write(token)

        t.upload(local_file_path)
        contents = t.list_contents()

        found = [entry for entry in contents if entry.name == filename]
        assert len(found) > 0, 'The uploaded test file was not found, should be found'

        # remove test file locally
        try:
            os.remove(local_file_path)
        except Exception:
            pass

        # remove test file on cloud
        t.remove(f'/{filename}')
        contents = t.list_contents()
        found = [entry for entry in contents if entry.name == filename]
        assert len(found) == 0, 'The contents should be empty'


    # def test_i_can_download_new_orders_zip(self):
    #     '''Tests downloading contents to local zip'''
    #     t = DropboxApp()
    #     dest_filename = f'test_dbx_{timezone.now()}.zip'
    #     path = os.path.join(settings.MEDIA_ROOT,dest_filename)
    #     remote_path = f'/{settings.NEW_ORDERS_FOLDER}'
    #     t.download_all_as_zip(path,remote_path)
    #     assert False

    def test_downloaded_new_orders_match_downloaded_file_metadata(self):
        # To replace test_i_can_download_new_orders_zip
        assert True

    # @pytest.mark.skip(reason="todo")
    # def test_orderform_model_has_reference_for_dropbox_file(self):
    #     assert True

    # @pytest.mark.skip(reason="todo")
    # def test_i_remove_file_from_dropbox_when_order_processed(self):
    #     '''E2E order process and locally stored temp files are removed'''
    #     assert False
