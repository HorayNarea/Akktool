from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=500)
    MemberID = models.PositiveIntegerField()
    birthdate = models.DateField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    organisation = models.CharField(max_length=100)
    haspayed = models.BooleanField()
