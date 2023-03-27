from django.shortcuts import render, redirect, resolve_url
from apps.scheduler.ssr.views import dashboard
from apps.users.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # TODO
        # Confirm if the username exists
        if User.objects.filter(username=username).exists():
            # TODO
            # Use the email to authenticate and login the user
            user = authenticate(request, username=User.objects.get(username=username).email, password=password)
            if user is not None:
                login(request, user)
                return redirect(resolve_url(dashboard))
            else:
                return render(request, 'login.html', {"message": "ID Or Password Is Incorrect"})
        else:
            return render(request, 'login.html', {"message": "ID Or Password Is Incorrect"})
    return render(request, 'login.html')


@login_required()
def users(request):
    if request.user.is_superuser:
        all_users = User.objects.all()
        return render(request, 'users.html', {"users": all_users})
    else:
        return redirect(resolve_url(dashboard))
