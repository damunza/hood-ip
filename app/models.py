from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Business(models.Model):
    business_name= models.CharField(max_length=50)
    email = models.EmailField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey('app.Hood', on_delete=models.CASCADE, related_name='jirani')

    def __str__(self):
        return self.business_name

class Hood(models.Model):
    location_choices = (
        (1, 'Nairobi'),
        (2, 'Kajiado'),
        (3, 'Mombasa'),
        (4, 'Kilifi'),
        (5, 'kiambu'),
    )
    name= models.CharField(max_length=50)
    location = models.CharField(max_length=50, choices=location_choices)
    occupants = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



