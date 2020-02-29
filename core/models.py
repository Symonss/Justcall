from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length = 100)
    abvr = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_auser = models.BooleanField(default=False)
    is_nuser = models.BooleanField(default=False)

class Extension(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    department  = models.ForeignKey(Department, on_delete = models.CASCADE, default = 1, blank = True, null = True)


    def __str__(self):
        return self.name
