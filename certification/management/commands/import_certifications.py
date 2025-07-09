import json
from django.core.management.base import BaseCommand
from certification.models import Certifications, Category, Topic, Institutions, Prerequisites, Languages


class Command(BaseCommand):
    help = 'Importe des certifications depuis un fichier JSON'


    def handle(self, *args, **kwargs):

        try:
            with open('data/certifications.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Fichier  non trouvé."))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Erreur lors de la lecture du fichier JSON."))
            return

        for item in data:
            name = item['name'].strip()

            # Récupérer l'institution
            institution_name = item.get('institution')
            institution = None
            if institution_name:
                try:
                    institution = Institutions.objects.get(name=institution_name)
                except Institutions.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Institution '{institution_name}' non trouvée pour la certification '{name}'. Ignoré."))
                    continue

            # Créer ou mettre à jour la certification
            certification, created = Certifications.objects.update_or_create(
                name=name,
                defaults={
                    'description': item.get('description'),
                    'level_of_difficulty': item.get('level_of_difficulty', '0'),
                    'price': item.get('price', 0),
                    'duration_of_validity': item.get('duration_of_validity'),
                    'exam_site': item.get('exam_site'),
                    'link': item.get('link'),
                    'discounts': item.get('discounts'),
                    'institution': institution,
                }
            )

            # Gestion des relations ManyToMany
            # Catégories
            for cat in item.get('categories', []):
                try:
                    category = Category.objects.get(name=cat.strip())
                    certification.category.add(category)
                except Category.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Catégorie '{cat}' non trouvée."))

            # Topics
            for top in item.get('topics', []):
                try:
                    topic = Topic.objects.get(name=top.strip())
                    certification.topic.add(topic)
                except Topic.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Topic '{top}' non trouvé."))

            # Prérequis
            for prereq in item.get('prerequisites', []):
                try:
                    prerequisite = Prerequisites.objects.get(title=prereq.strip())
                    certification.prerequisites.add(prerequisite)
                except Prerequisites.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Prérequis '{prereq}' non trouvé."))

            # Langues
            for lang in item.get('languages', []):
                try:
                    language = Languages.objects.get(name=lang.strip())
                    certification.languages.add(language)
                except Languages.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Langue '{lang}' non trouvée."))

            status = "créée" if created else "mise à jour"

        self.stdout.write(self.style.SUCCESS("Import des certifications terminé."))