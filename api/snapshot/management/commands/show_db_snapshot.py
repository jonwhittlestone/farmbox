import logging
from django.core.management.base import BaseCommand
from tabulate import tabulate
from snapshot.models import calculate_model_signature as hydrate_signature

logger = logging.getLogger(__name__)


def formatted(snapshot=None):

    table = [
        [
            "model",
            snapshot.get("model"),
        ],
        ["id", snapshot.get("id")],
        [
            "before_or_after_migration",
            snapshot.get("before_or_after_migration"),
        ],
        [
            "signature",
            snapshot.get("signature"),
        ],
        [
            "match?",
            snapshot.get("match"),
        ],
    ]
    return tabulate(table)


def calculate_snapshots():
    ret = []
    example_objects = [
        {
            "model": "Order",
            "id": 1864,
            "before_or_after_migration": "-",
            "signature": "",
            "match": "-",
        }
    ]
    for obj in example_objects:
        obj["signature"] = hydrate_signature(obj)
        ret.append({"output": formatted(obj)})
    return ret


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("CALLED: show_db_snapshot")
        snapshots: list = calculate_snapshots()
        for s in snapshots:
            self.stdout.write(s.get("output"))

        logger.info("FINISHED: show_db_snapshot")
