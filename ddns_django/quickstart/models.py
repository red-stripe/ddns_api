from django.db import models

# Create your models here.
class Node(models.Model):
    nodename = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    ip4 = models.CharField(max_length=13)
    location = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.name
