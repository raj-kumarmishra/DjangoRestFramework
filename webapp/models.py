from django.db import models

# Create your models here.

class employees(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    empid = models.IntegerField(max_length=100)

    def __str__(self):
        return self.first_name
