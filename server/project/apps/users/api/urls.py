from .views import signup, verify_user, update_profile_picture, change_status, delete_user
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('verify-user/', verify_user, name='verify_user'),
    path('update-photo/', update_profile_picture, name='update_profile_picture'),
    path('change-status/', change_status, name='change_status'),
    path('delete-user/', delete_user, name='delete_user'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
