from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('client', 'client'),
        ('owner', 'owner'),
    )
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Car(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=80)
    year = models.PositiveIntegerField()
    TYPE_CHOICES = (
        ('Дизель', 'Дизель'),
        ('Газ', 'Газ'),
        ('Бензин', 'Бензин'),
    )
    fuel_type = models.CharField(max_length=40,choices=TYPE_CHOICES)
    transmission = models.CharField(max_length=80)
    mileage = models.PositiveSmallIntegerField(verbose_name='Пробег', default=0)
    price = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    images = models.ImageField()
    seller = models.ForeignKey(UserProfile,related_name='user', on_delete=models.CASCADE)


class CarPhotos(models.Model):
    home_photo = models.ForeignKey(Car,related_name='car_photos',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')


class Auction(models.Model):
    car = models.ForeignKey(Car, related_name='car',on_delete=models.CASCADE)
    start_price = models.PositiveSmallIntegerField(default=0)
    min_price = models.PositiveSmallIntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    STATUS_CHOICES = (
        ('active', 'active'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    )
    status = models.CharField(max_length= 30,choices= STATUS_CHOICES)


class Bid(models.Model):
    auction = models.ForeignKey(Auction, related_name='auction',on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, related_name='client',on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile,related_name='users',on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile,related_name='buyer',on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)







