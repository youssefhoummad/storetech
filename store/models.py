from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name



class Device(models.Model):
    category = models.ForeignKey(Category, related_name='devices', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    brand =  models.ForeignKey(Brand, related_name='devices', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    picture = models.URLField()
    quantity =  models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{} {}".format(self.brand, self.name)    



class Purchase(models.Model):
    device = models.ForeignKey(Device, related_name='purchases', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0.0)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " purchase " + self.device.name
