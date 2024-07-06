from django.db import models

# Create your models here.
class Trader  (models.Model) :
    traders_id = models.IntegerField()
    traders_fullname = models.CharField(max_length=40)
    traders_email = models.EmailField()
    traders_location = models.TextField()
    traders_password = models.PositiveBigIntegerField()
