from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError

class Command(BaseCommand):
    """django command wait for database"""
    def handle(self,*args,**options):
        self.stdout.write('Waiting for databse.......')
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except(Psycopg20pError,OperationalError):
                self.stdout.write('Database failed, wait for 1 s')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))