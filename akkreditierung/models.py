# coding: UTF-8
from django.db import models

class Member(models.Model):
    MemberID = models.PositiveIntegerField('Mitgliedsnummer', primary_key=True)
    firstname = models.CharField('Vorname', max_length=100)
    middlename = models.CharField('weitere Vornamen', max_length=500, blank=True, null=True)
    lastname = models.CharField('Nachname', max_length=100)
    birthdate = models.DateField('Geburtsdatum')
    address = models.CharField('Anschrift', max_length=500)
    city = models.CharField('Ort', max_length=100)
    zipcode = models.PositiveIntegerField('PLZ')
    organisation = models.CharField('Gliederung', max_length=100, blank=True, null=True)
    haspaid = models.BooleanField('hat bezahlt?')
    debt = models.DecimalField('Offene Beiträge', max_digits=6, decimal_places=2, blank=True, null=True)
    akk = models.BooleanField('ist akkreditiert?')
    def __unicode__(self):
        return str(self.MemberID) + ' ' + self.firstname + ' ' + self.middlename + ' ' + self.lastname
