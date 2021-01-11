from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

Gender = (
    (1, "Choose gender"),
    (2, "Male"),
    (3, "Female"),
)

class Clients(models.Model):
    client = models.ForeignKey(User,related_name="users",on_delete=models.CASCADE)
    gender = models.IntegerField(choices=Gender, default=1)
    nationality = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.client}"




