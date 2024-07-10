from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary= models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


    def __str__(self):
        return self.summary
