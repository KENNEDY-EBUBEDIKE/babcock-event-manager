from django.shortcuts import render, redirect, resolve_url
from apps.scheduler.ssr.views import dashboard
from apps.users.models import User
from django.contrib.auth import authenticate, login


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
