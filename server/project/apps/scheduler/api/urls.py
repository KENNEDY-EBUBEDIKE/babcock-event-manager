from django.urls import path
from django.conf import settings
from .views import event, events, create_poll

urlpatterns = [
    path('event/', event, name='event'),
    path('events/', events, name='events'),
    path('poll/', create_poll, name='create_poll'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
