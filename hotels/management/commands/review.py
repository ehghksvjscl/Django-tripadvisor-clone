import random
import csv
import os

from django.core.management.base import BaseCommand, no_translations
from hotels.models import *
from account.models import *
from review.models import *

class Command(BaseCommand):

    @no_translations
    def handle(self, *args, **options):
        CSV_PATH = [f"{os.path.dirname( os.path.abspath( __file__ ) )}/db/hawaii.csv"]
        CSV_PATH.append(f"{os.path.dirname( os.path.abspath( __file__ ) )}/db/hawaii2.csv")
        CSV_PATH.append(f"{os.path.dirname( os.path.abspath( __file__ ) )}/db/hawaii3.csv")
        CSV_PATH.append(f"{os.path.dirname( os.path.abspath( __file__ ) )}/db/hawaii4.csv")
        CSV_PATH.append(f"{os.path.dirname( os.path.abspath( __file__ ) )}/db/hawaii5.csv")
        CSV_PATH.append(f"{os.path.dirname( os.path.abspath( __file__ ) )}/db/hawaii6.csv")


        for CSV in CSV_PATH:
            with open(CSV) as in_file:
                data_reader = csv.reader(in_file)
                for row in data_reader:
                    english_name = row[0]
                    user_name    = row[1]
                    stars        = row[2]
                    review_title = row[3]
                    review_text  = row[4]  
                    
                    if Hotel.objects.filter(hotel_detail__english_name = english_name).exists():
                        try:
                            user = User.objects.get(name = user_name)
                        except:
                            User(
                                name= user_name
                            ).save()
                        Review(
                            user=User.objects.get(name=user_name),
                            hotel=Hotel.objects.filter(hotel_detail__english_name=english_name)[0],
                            star=stars,
                            title=review_title,
                            text=review_text
                        ).save()
                    