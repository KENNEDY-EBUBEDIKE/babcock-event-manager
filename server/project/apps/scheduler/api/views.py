from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.scheduler.models import Event
from apps.scheduler.serializers import EventSerializer
from datetime import datetime


@api_view(["GET"])
def events(request):
    return Response(
        data={
            "success": True,
            "events": EventSerializer(Event.objects.all(), many=True).data
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST", "PATCH", "DELETE"])
def event(request):
    if request.method == "POST":
        new_event = Event()
        new_event.title = request.data['title']
        new_event.start = int(request.data['start'])
        new_event.backgroundColor = request.data['background_color']
        new_event.borderColor = request.data['border_color']
        try:
            new_event.save()
        except Exception as e:
            return Response(
                data={
                    "success": False,
                    "message": e.args[0]
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            data={
                "success": True,
                "message": "Created Successfully",
                "event": EventSerializer(new_event).data
            },
            status=status.HTTP_200_OK,
        )
    elif request.method == "PATCH":
        event = Event.objects.get(id=request.data['id'])
        event_serializer = EventSerializer(instance=event, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(
                data={
                    "success": True,
                    "message": "Adjusted Successfully"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data={
                    "success": False,
                    "message": event_serializer.errors
                },
                status=status.HTTP_200_OK,
            )
    elif request.method == "DELETE":
        print(request.data)
        event = Event.objects.get(id=request.data['id'])
        event.delete()
        return Response(
            data={
                "success": True,
                "message": "Deleted Successfully"
            },
            status=status.HTTP_200_OK,
        )
