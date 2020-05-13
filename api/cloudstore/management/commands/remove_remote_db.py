import logging
from django.core.management.base import BaseCommand
from cloudstore.models import DropboxApp, remove_remote_db

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        """ Remove the remote db """
        if remove_remote_db():
            self.stdout.write(self.style.SUCCESS('Removed DB to Dropbox'))
        else:
            self.stdout.write(self.style.SUCCESS('There was no remote DB to remove'))
