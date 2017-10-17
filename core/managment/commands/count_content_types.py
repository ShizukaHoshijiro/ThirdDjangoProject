from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType

'''По задумке это должно добавить комманду manage.py count_content_types'''

class Command(BaseCommand):
    def handle(self, *args, **options):
        for a in ContentType.objects.all():
            print("id: ", a.id, " model_name: ", a.model)