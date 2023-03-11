from .views import verify_user, signup
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('verify_user/', verify_user, name='verify_user'),
    path('signup/', signup, name='signup'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
