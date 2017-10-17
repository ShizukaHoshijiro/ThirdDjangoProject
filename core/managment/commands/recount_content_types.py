from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        for content_type in ContentType.objects.all():
            print("id:", content_type.id, "; model_name:", content_type.model)