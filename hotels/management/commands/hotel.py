import random
import csv
import os

from django.core.management.base import BaseCommand, no_translations
from hotels import models
from hotels.utils import create_date

class Command(BaseCommand):

    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        PATH = (f"{os.path.dirname( os.path.abspath( __file__ ) )}/db/trip_total.csv")
        CSV_PATH_PRODUCTS = PATH
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)
            for row in data_reader:
                stars = row[12].split("뿌")
                place = 0.0
                cleanliness = 0.0
                service = 0.0
                price = 0.0
                try:
                    place = float(stars[0])
                    cleanliness = float(stars[1])
                    service = float(stars[2])
                    price = float(stars[3])
                except (IndexError,ValueError):
                    pass

                star = models.Star.objects.create(
                    place=place,
                    cleanliness=cleanliness,
                    service=service,
                    price=price
                )

                #호텔 디테일 create
                price = 0
                price_sale = 0
                if row[2] == "":
                    price = 0
                    price_sale = 0
                else:
                    price = row[2]
                    price_sale = row[3]

                start_date,end_date = create_date()
                hotel_detail = models.HotelDetail.objects.create(
                    hotel_rating =random.randint(3,5),
                    english_name=row[9],
                    address=row[10],
                    content=row[16],
                    price=int(price),
                    price_sale=int(price_sale),
                    provider_logo = row[1],
                    label= row[6],
                    star_id=star.id,
                    reservation_start_at = start_date,
                    reservation_end_at = end_date,
                )

                #호텔 create
                hotel = models.Hotel.objects.create(
                    country_id=1,
                    city_id=1,
                    name=row[0],
                    user_rating=float(row[7]),
                    flat=row[8],
                    hotel_detail=hotel_detail,

                )

                #호텔 image craete
                images = row[11].split("뿌")
                for img in images:
                    if img != "":
                        image = models.Image.objects.create(
                            image_url=img
                        )
                        
                        hotel_image = models.HotelImage.objects.create(
                            hotel_detail=hotel_detail,
                            image=image
                        )

                #호텔 facility craete
                facilies = row[13].split("뿌")
                for f in facilies:
                    if f != "":
                        facility = models.Facility.objects.get(name=f)
                        
                        models.HotelFacility.objects.create(
                            facility=facility,
                            hotel_detail=hotel_detail
                        )

                #호텔 amanity craete
                amanities = row[14].split("뿌")
                for a in amanities:
                    if a != "":
                        amanity = models.Amenity.objects.get(name=a)
                        
                        models.HotelAmenity.objects.create(
                            amenity=amanity,
                            hotel_detail=hotel_detail
                        )

                #호텔 roomtype craete
                roomtypes = row[15].split("뿌")
                for r in roomtypes:
                    if r != "":
                        roomtype = models.Roomtype.objects.get(name=r)
                        
                        models.HotelRoomtype.objects.create(
                            roomtype=roomtype,
                            hotel_detail=hotel_detail
                        )

                        
