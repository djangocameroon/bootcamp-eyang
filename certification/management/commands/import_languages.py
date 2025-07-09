# myapp/management/commands/importer_languages.py
import json
from django.core.management.base import BaseCommand
from certification.models import Languages  # Remplace 'myapp' par le nom de ton application

class Command(BaseCommand):
    help = 'Importe les langues depuis un fichier JSON'

    def handle(self, *args, **kwargs):
        with open('data/languages.json', 'r', encoding='utf-8') as fichier:
            data = json.load(fichier)

        for item in data:
            Languages.objects.create(
                code=item['code'],
                name=item['name']
            )
        self.stdout.write(self.style.SUCCESS("✅ Import des langues terminé avec succès."))