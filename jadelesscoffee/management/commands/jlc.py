from django.core.management.base import BaseCommand
from django.conf import settings

from jadelesscoffee.utils import compile_all

class Command(BaseCommand):
  def handle(self, *args, **options):
    print "Compiling jade, less, and coffee files..."
    compile_all()
