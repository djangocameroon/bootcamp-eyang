# myapp/management/commands/testcmd.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("✅ Commande test exécutée avec succès !")