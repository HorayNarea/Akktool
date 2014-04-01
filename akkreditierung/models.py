# coding=UTF-8
from django.db import models

class Member(models.Model):
    firstname = models.CharField('Vorname', max_length=100)
    lastname = models.CharField('Nachname', max_length=100)
    middlename = models.CharField('zusätzliche Vornamen', max_length=500)
    MemberID = models.PositiveIntegerField(primary_key=True)
    birthdate = models.DateField('Geburtsdatum')
    address = models.CharField('Anschrift', max_length=500)
    city = models.CharField('Ort', max_length=100)
    zipcode = models.PositiveIntegerField('PLZ')
    organisation = models.CharField('LV', max_length=100)
    haspayed = models.BooleanField('hat bezahlt?')
