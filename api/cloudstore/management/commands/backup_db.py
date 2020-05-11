import logging
from django.core.management.base import BaseCommand
from cloudstore.models import DropboxApp

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        """ backup_db"""
        logger.info("CALLED: backup_db ")
        d = DropboxApp()
        d.backup_db()
        self.stdout.write(self.style.SUCCESS('Backed up DB to Dropbox'))
