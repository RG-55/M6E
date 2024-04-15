from django.db import models

# Create your models here.

    
class Account(models.Model):
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    objects = models.Manager()
    def getUsername(self):
        return self.name
    def getPassword(self):
        return self.password
    def __str__(self):
        return str(self.pk) + ": " + self.name