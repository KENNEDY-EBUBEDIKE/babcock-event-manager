from django.db import models
from datetime import datetime
from pytz import timezone
from django.db.models import Count


class Event(models.Model):
    title = models.CharField(max_length=255)
    start = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    end = models.BigIntegerField(blank=True, null=True)
    actual_start_datetime = models.DateTimeField(auto_now_add=False, null=True)
    actual_end_datetime = models.DateTimeField(auto_now_add=False, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True, default="UP COMING")
    physical_venue = models.ForeignKey('Venue', on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    meeting_link = models.CharField(max_length=255, blank=True, null=True)
    event_type = models.CharField(max_length=255, blank=True, null=True)
    backgroundColor = models.CharField(max_length=255, null=True, blank=True)
    borderColor = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='events', null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_from_academic_calendar = models.BooleanField(default=False)
    has_poll = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def set_venue(self, venue):
        if self.event_type == "physical":
            self.physical_venue = Venue.objects.get(name=venue)
        elif self.event_type == "virtual":
            self.meeting_link = venue
        self.save()

    def get_venue(self):
        if self.event_type == "physical":
            return self.physical_venue
        elif self.event_type == "virtual":
            return self.meeting_link

    def save(self, *args, **kwargs):
        self.actual_start_datetime = datetime.fromtimestamp(int(self.start) / 1000, tz=timezone('Africa/Lagos'))
        if self.end:
            self.actual_end_datetime = datetime.fromtimestamp(int(self.end) / 1000, tz=timezone('Africa/Lagos'))
        super(Event, self).save(*args, **kwargs)

    def get_positive_polls(self):
        if self.has_poll:
            return self.polls.filter(attending__iexact='yes').aggregate(Count('id'))['id__count']

    def get_negative_polls(self):
        if self.has_poll:
            return self.polls.filter(attending__iexact='no').aggregate(Count('id'))['id__count']

    def get_undecided_polls(self):
        if self.has_poll:
            return self.polls.filter(attending__iexact='maybe').aggregate(Count('id'))['id__count']


class Poll(models.Model):
    ATTENDING_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('MAYBE', 'Maybe')
    )

    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='polls')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='polls')
    attending = models.CharField(max_length=5, choices=ATTENDING_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.event.title} - {self.attending}'

    class Meta:
        unique_together = (('event', 'user'),)


class Venue(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    capacity = models.IntegerField(null=True, blank=True)
    coordinate = models.CharField(max_length=255, blank=True, null=True)
    features = models.JSONField(default=dict)

    def __str__(self):
        return self.name
