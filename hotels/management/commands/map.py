import requests
import random
import csv
import os
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand, no_translations
from hotels.models import *
from account.models import *
from review.models import *

class Command(BaseCommand):

    @no_translations
    def handle(self, *args, **options):
        headers = {"accept-agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko)\
                Version/11.0 Mobile/15A5341f Safari/604.1"}

        hotels = HotelDetail.objects.all()

        for hotel in hotels:
            base_url = f"https://maps.googleapis.com/maps/api/geocode/xml?address={hotel.address}&key=AIzaSyBairBfk9muGSPT7VWPl1oaFusga4xw6lw"
            resp = requests.get(base_url, headers=headers)
            html = BeautifulSoup(resp.text, "lxml")
            lat = html.select("location > lat")
            lng = html.select("location > lng")
            try:
                hotel.lat = lat[0].get_text()
                hotel.lng = lng[0].get_text()
            except IndexError:
                hotel.lat = ""
                hotel.lng = ""
                
            hotel.save()