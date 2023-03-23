from django.contrib import admin
from apps.scheduler.models import Event
from apps.users.models import User

# Register your models here.
admin.site.register(Event)
admin.site.register(User)
