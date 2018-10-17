from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Business(models.Model):
    business_name= models.CharField(max_length=50)
    email = models.EmailField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey('app.Hood', on_delete=models.CASCADE, related_name='jirani')
