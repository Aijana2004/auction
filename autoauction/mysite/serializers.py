from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class CarPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarPhotos
        fields = ['image']


class CarListSerializers(serializers.ModelSerializer):
    car_photos = CarPhotosSerializers(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id','brand', 'model','year','seller','car_photos','description','price',
                  'mileage','transmission','fuel_type']


class CarCreateSerializers(serializers.ModelSerializer):
    car_photos = CarPhotosSerializers(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id','brand', 'model','year','seller','car_photos','description','price',
                  'mileage','transmission','fuel_type']


class AuctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id','car','start_price','min_price','start_time','end_time','status']


class AuctionCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id','car','start_price','min_price','start_time','end_time','status']


class BidSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y ')

    class Meta:
        model = Bid
        fields = ['id','auction','buyer','amount','created_at',]


class BidCreateSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y ')
    buyer = UserProfileSimpleSerializers()

    class Meta:
        model = Bid
        fields = ['id','auction','buyer','amount','created_at',]


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

