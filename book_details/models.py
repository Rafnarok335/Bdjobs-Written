from django.db import models

# Create your models here.


class Book(models.Model):
    serial_number = models.AutoField(primary_key=True, default=0)
    title = models.CharField(max_length=256)
    publisher_name = models.CharField(max_length=256)
    publisher_age = models.IntegerField(default=0)
    page_no = models.IntegerField(default=0)
    publication_date = models.DateField()
    genre = models.CharField(max_length=256)
