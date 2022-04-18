from django.db import models


# Create your models here.
class Greeting(models.Model):
    message = models.CharField(max_length=70)

    def __str__(self):
        return self.message
