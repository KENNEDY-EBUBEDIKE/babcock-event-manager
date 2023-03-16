from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.scheduler.models import Event
from apps.scheduler.serializers import EventSerializer


@login_required()
def dashboard(request):
    return render(request, 'blank.html')


@login_required()
def event_calendar(request):
    events = Event.objects.all()
    return render(request, 'schedule-event.html', {"events": events})
