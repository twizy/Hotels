from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Base.models import Clients

# Create your models here.

# RoomType = (
#     (1, "Room type"),
#     (2, "Single occupation"),
#     (3, "Double occupation"),
#     (4, "Both occupation"),
# )

# Gender = (
#     (1, "Choose gender"),
#     (2, "Male"),
#     (3, "Female"),
# )

class Genders(models.Model):
    gender = models.CharField(max_length=64,default="Male", blank=True)

    def __str__(self):
        return f"{self.gender}"

class RoomType(models.Model):
    room = models.CharField(max_length=64,default="Single occupation", blank=True)

    def __str__(self):
        return f"{self.room}"

class Provinces(models.Model):
    province = models.CharField(max_length=64,null=True, blank=True)

    def __str__(self):
        return f"{self.province}"

class States(models.Model):
    state = models.CharField(max_length=64,null=True, blank=True)
    province = models.ForeignKey(Provinces, related_name='provinces', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.state}"

class Quarters(models.Model):
    quarter = models.CharField(max_length=64,null=True, blank=True)
    state = models.ForeignKey(States,related_name='states',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quarter}"

class Hotels(models.Model):
    name = models.CharField(max_length=64)
    province = models.ForeignKey(Provinces, related_name='provinc', on_delete=models.CASCADE)
    photo_outside = models.ImageField(upload_to='Images/hotels/', null=True, blank=True)
    photo_inside = models.ImageField(upload_to='Images/hotels/', null=True, blank=True)
    photo_room = models.ImageField(upload_to='Images/hotels/', null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

class Rooms(models.Model):
    hotel = models.ForeignKey(Hotels,related_name='hotel',on_delete=models.CASCADE)
    room = models.ForeignKey(RoomType,related_name='room_type',on_delete=models.CASCADE)
    room_number = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.room}"

class Reservations(models.Model):
    client = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,related_name='hotels',on_delete=models.CASCADE)
    room_number = models.ForeignKey(Rooms,related_name='rooms',on_delete=models.CASCADE)
    taken = models.BooleanField(True)
    transaction_code = models.CharField(max_length=64)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.client} has booked {self.room_number} in {self.hotel}"

