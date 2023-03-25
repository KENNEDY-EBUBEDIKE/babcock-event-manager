from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from apps.scheduler.models import Event, Venue, Poll
from apps.users.models import User


# @login_required()
def dashboard(request):
    if request.user.is_authenticated:
        users_count = User.objects.all().count()
        all_events_count = Event.objects.all().count()
        polled_events_count = Event.objects.filter(has_poll=True).count()
        recent_events = Event.objects.all().order_by('actual_start_datetime')[:5]
        return render(request, 'dashboard.html', {
            "users_count": users_count,
            "all_events_count": all_events_count,
            "polled_events_count": polled_events_count,
            "recent_events": recent_events,
        })
    else:
        return redirect('/users/login/')


@login_required()
def event_calendar(request):
    venues = Venue.objects.all()
    return render(request, 'schedule-event.html', {"venues": venues})


@login_required()
def meeting_log(request):
    events = Event.objects.all().order_by('actual_start_datetime')
    return render(request, 'meeting-log.html', {"events": events})


@login_required()
def polls(request):
    events = request.user.events.all().order_by('actual_start_datetime')
    return render(request, 'polls.html', {"events": events})


@login_required()
def add_venue(request):
    if request.method == "POST":
        new_venue = Venue()
        new_venue.name = request.POST.get("name").upper()
        new_venue.capacity = request.POST.get("capacity")
        new_venue.coordinate = request.POST.get("coordinate", None)
        new_venue.save()
        return redirect(reverse(event_calendar))
