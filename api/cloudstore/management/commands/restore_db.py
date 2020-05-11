import logging
from django.core.management.base import BaseCommand
from cloudstore.models import DropboxApp

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        """ restore_db"""
        logger.info("CALLED: restore_db ")
        d = DropboxApp()
        d.restore_db()
        self.stdout.write(self.style.SUCCESS('Restored DB from Dropbox'))
