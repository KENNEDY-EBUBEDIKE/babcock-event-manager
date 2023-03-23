from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from apps.users.models import StaffProfile, StudentProfile, User
from django.db import IntegrityError
import json


@api_view(["POST"])
def signup(request):
    try:
        new_user = User.objects.create_user(
            email=request.data['email'],
            username=request.data['id'],
            password=request.data['password'],
        )
        new_user.save()
    except (IntegrityError, ValueError) as e:
        return Response(
            data={
                "success": False,
                "message": e.args[0]
            },
            status=status.HTTP_200_OK,
        )

    new_user.first_name = request.data['first_name']
    new_user.surname = request.data['last_name']
    new_user.save()

    if request.data['is_staff'] == "true":
        new_user.is_staff = True
        staff = StaffProfile.objects.create(
            user=new_user,
            staff_id=request.data['id'])
        staff.save()
    else:
        new_user.is_staff = False
        student = StudentProfile.objects.create(
            user=new_user,
            matric_number=request.data['id'])
        student.save()

    new_user.save()
    return Response(
        data={
            "success": True,
            "message": "OK"
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def verify_user(request):
    username = request.data['username']
    password = request.data['password']

    # TODO
    # Confirm if the username exists
    if User.objects.filter(username=username).exists():
        # TODO
        # Use the email to authenticate and login the user
        user = authenticate(request, username=User.objects.get(username=username).email, password=password)
        if user is not None:
            return Response(
                data={
                    "success": True,
                    "message": "User Verified"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data={
                    "success": False,
                    "message": "ID Or Password Is Incorrect"
                },
                status=status.HTTP_200_OK,
            )
    else:
        return Response(
            data={
                "success": False,
                "message": "ID Or Password Is Incorrect"
            },
            status=status.HTTP_200_OK,
        )
