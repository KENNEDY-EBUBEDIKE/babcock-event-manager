from django.urls import path
from django.conf import settings
from .views import dashboard, event_calendar, meeting_log, add_venue, polls

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('schedule-event', event_calendar, name='event_calendar'),
    path('meeting-log', meeting_log, name='meeting_log'),
    path('add-venue', add_venue, name='add_venue'),
    path('polls', polls, name='polls'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
