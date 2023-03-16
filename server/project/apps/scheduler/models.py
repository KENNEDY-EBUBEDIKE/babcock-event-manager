from django.db import models
from datetime import datetime


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    start = models.BigIntegerField(blank=True, null=True)
    end = models.BigIntegerField(blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    venue_coordinate = models.BigIntegerField(blank=True, null=True)
    backgroundColor = models.CharField(max_length=255, null=True, blank=True)
    borderColor = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
