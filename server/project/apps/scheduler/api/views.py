from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.scheduler.models import Event, Venue
from apps.scheduler.serializers import EventSerializer
from datetime import datetime
from pytz import timezone


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
        start_datetime = datetime.fromtimestamp(int(request.data['start']) / 1000, tz=timezone('Africa/Lagos'))
        start_date = start_datetime.date()
        if Event.objects.filter(actual_start_datetime__date=start_date, is_from_academic_calendar=True).exists():
            return Response(
                data={
                    "success": False,
                    "message": "An Event From the Academic Calendar Has been scheduled For this Day"
                },
                status=status.HTTP_200_OK,
            )

        new_event = Event()
        new_event.title = request.data['title']. upper()
        new_event.start = int(request.data['start'])

        new_event.description = request.data['description']
        new_event.event_type = request.data['event_type']
        new_event.created_by = request.user

        new_event.backgroundColor = request.data['background_color']
        new_event.borderColor = request.data['border_color']
        try:
            new_event.save()
            new_event.set_venue(request.data['venue'])
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
        Event.objects.get(id=request.data['id']).delete()
        return Response(
            data={
                "success": True,
                "message": "Deleted Successfully"
            },
            status=status.HTTP_200_OK,
        )
