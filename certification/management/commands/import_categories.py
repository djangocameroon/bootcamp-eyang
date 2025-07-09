import json
from django.core.management.base import BaseCommand
from certification.models import Category


class Command(BaseCommand):
    help = 'Importe des catégories depuis un fichier JSON'


    def handle(self, *args, **kwargs):


        try:
            with open('data/categories.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Fichier non trouvé."))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Erreur lors de la lecture du fichier JSON."))
            return

        for item in data:
            category_name = item['name'].strip()
            if len(category_name) > 20:
                self.stdout.write(self.style.WARNING(f"Nom trop long (max 20) : {category_name}"))
                continue

            Category.objects.update_or_create(
                name=category_name
            )

        self.stdout.write(self.style.SUCCESS("Import des catégories terminé."))