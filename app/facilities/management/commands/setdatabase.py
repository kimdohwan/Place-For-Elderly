from django.core.management import BaseCommand

from ...utils.open_api import set_database


class Command(BaseCommand):
    def handle(self, *args, **options):
        set_database()
