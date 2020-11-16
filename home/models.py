from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class seeker(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    dname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.dname

class donor(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    dname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.dname

class blooddonor(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    blood = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.name


class bloodseeker(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    blood = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.name


