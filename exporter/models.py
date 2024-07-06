from django.db import models

# Create your models here.
class Exporter  (models.Model) :
    exporter_id = models.IntegerField()
    exporter_location = models.TextField()
    exporter_name = models.CharField(max_length=20)
