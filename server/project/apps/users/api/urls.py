from .views import signup, verify_user
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('verify-user/', verify_user, name='verify_user'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
