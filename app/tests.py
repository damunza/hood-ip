from django.test import TestCase
from .models import *

# Create your tests here.

class EventTest(TestCase):

    def setUp(self):
        self.area = Hood.objects.create(name='a', location=1)
        self.event = Event.objects.create(affected='a',
                                          description='b',
                                          area=self.area)

    def test_instance(self):
        self.assertTrue(isinstance(self.event, Event))

    def test_get_event(self):
        self.event.save()
        event = Event.get_event('a')
        self.assertTrue(len(event)>0)

class ServiceTest(TestCase):

    def setUp(self):
        self.area = Hood.objects.create(name='a', location=1)
        self.service = Service.objects.create(type='a',
                                              name='b',
                                              area= self.area)

    def test_instance(self):
        self.assertTrue(isinstance(self.service, Service))

    def test_get_service(self):
        self.service.save()
        service = Service.get_service('a')
        self.assertTrue(len(service)>0)

class ResidentTest(TestCase):

    def setUp(self):
        self.area = Hood.objects.create(id=1, name='a', location=1)
        self.user = User.objects.create(id=1, username='a')
        self.resident= Resident.objects.create(name=self.user,
                                               home=self.area,
                                               email='a@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.resident, Resident))

    def test_get_human(self):
        self.resident.save()
        human = Resident.get_human('a')
        self.assertTrue(len(human) > 0)

class HoodTest(TestCase):

    def setUp(self):
        self.area = Hood.objects.create(id=1, name='a', location=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.area,Hood))

    def test_get_hood(self):
        self.area.save()
        hood = Hood.get_hood('a')
        self.assertTrue(len(hood)>0)