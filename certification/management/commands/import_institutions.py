import json
from django.core.management.base import BaseCommand
from certification.models import Institutions


class Command(BaseCommand):
    help = 'Importe des institutions depuis un fichier JSON'


    def handle(self, *args, **kwargs):


        try:
            with open('data/institutions.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Fichier  non trouvé."))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Erreur lors de la lecture du fichier JSON."))
            return

        for item in data:
            Institutions.objects.update_or_create(
                name=item['name'],
                defaults={
                    'accepted_zones': item.get('accepted_zones', ''),
                    'about': item.get('about', '')
                }
            )

        self.stdout.write(self.style.SUCCESS("Import terminé."))