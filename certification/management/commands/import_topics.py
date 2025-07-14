import json
from django.core.management.base import BaseCommand
from certification.models import Topic


class Command(BaseCommand):
    help = 'Importe des topics depuis un fichier JSON'


    def handle(self, *args, **kwargs):


        try:
            with open('data/topics.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Fichier  non trouvé."))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Erreur lors de la lecture du fichier JSON."))
            return

        for item in data:
            topic_name = item['name'].strip()
            if len(topic_name) > 20:
                self.stdout.write(self.style.WARNING(f"Nom trop long (max 20) : {topic_name}"))
                continue

            Topic.objects.update_or_create(
                name=topic_name
            )

        self.stdout.write(self.style.SUCCESS("Import des topics terminé."))