from django.db import models

# Create your models here.

class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
