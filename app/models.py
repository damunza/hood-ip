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
        (5, 'Kiambu'),
    )
    name= models.CharField(max_length=50)
    location = models.IntegerField(choices=location_choices)
    occupants = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @classmethod
    def get_hood(cls,jina):
        home = Hood.objects.filter(name__icontains=jina)
        return home

class Resident(models.Model):
    pic = models.ImageField(upload_to='images/')
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    id_number = models.IntegerField(default=0)
    email=models.EmailField()
    home = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username

    @classmethod
    def get_human(cls,jina):
        human= Resident.objects.filter(name__username__icontains = jina)
        return human

    @classmethod
    def change_hood(cls, iden, hood):
        person = Resident.objects.filter(name__username__icontains = iden)
        person.update(home = hood)
        for object in person:
            object.save()
        return person

class Service(models.Model):
    area = models.ForeignKey(Hood, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    contact = models.IntegerField(default=0)

    def __str__(self):
        return self.type

    @classmethod
    def get_service(cls,jina):
        service = Service.objects.filter(area__name__icontains= jina)
        return service

class Event(models.Model):
    affected = models.CharField(max_length=60)
    description= models.TextField()
    area = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return self.affected

    @classmethod
    def get_event(cls,jina):
        news = Event.objects.filter(area__name__icontains=jina)
        return news
