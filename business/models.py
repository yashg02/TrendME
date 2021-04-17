from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dashboard(models.Model):
        # fields of the model
    user = models.CharField(max_length=50,default="")
    title = models.CharField(max_length = 200)
    description = models.TextField()
    img = models.ImageField(upload_to = "images/")
    price = models.IntegerField(default=0)
    dprice = models.IntegerField(default=0)

    def __str__(self):
        return self.title