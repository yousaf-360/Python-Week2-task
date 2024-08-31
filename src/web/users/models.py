from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.user.first_name+" "+self.user.last_name}"

    
    