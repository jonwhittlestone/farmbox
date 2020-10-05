import os
from zipfile import ZipFile
import shutil
from pathlib import Path
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
        assert sorted(subfolders) == list(settings.CLOUD_SUBFOLDERS)



    # @pytest.mark.skip(reason="surpress during dev")
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

    def clean_up(self):
        t = DropboxApp()
        t.remove(settings.TESTING_ORDERS_REMOTE_PATH)

    @pytest.fixture
    def test_orders(self):
        t = DropboxApp()
        t.svc.files_create_folder_v2(settings.TESTING_ORDERS_REMOTE_PATH)
        t.upload(settings.SAMPLE_ORDER_SHEET_PATH,
                 settings.TESTING_ORDERS_REMOTE_PATH)

    def test_downloaded_orders_match_file_metadata(self, test_orders):
        t = DropboxApp()
        dest_filename = f'test_dbx_{timezone.now()}.zip'
        path = os.path.join(settings.MEDIA_ROOT,dest_filename)
        remote_path = settings.TESTING_ORDERS_REMOTE_PATH
        contents = t.download_all_as_zip(path,remote_path)

        # unzip and assert contents of zip matches contents
        with ZipFile(path, 'r') as zipObj:
            zipObj.extractall(settings.MEDIA_ROOT)

        self.clean_up()
        extracted_dir = os.path.join(settings.MEDIA_ROOT,settings.TESTING_ORDERS_DIRNAME)
        xlsx_files = Path(extracted_dir).glob("*.xlsx")
        xlsx_files = sorted([f.name for f in list(xlsx_files)])
        dropbox_contents = sorted([f.name for f in contents])
        assert len(xlsx_files) == len(dropbox_contents)
        assert xlsx_files == dropbox_contents

        os.remove(path)
        shutil.rmtree(extracted_dir)

    # @pytest.mark.skip(reason="todo")
    # def test_orderform_model_has_reference_for_dropbox_file(self):
    #     assert True

    # @pytest.mark.skip(reason="todo")
    # def test_i_remove_file_from_dropbox_when_order_processed(self):
    #     '''E2E order process and locally stored temp files are removed'''
    #     assert False
