from django.http import HttpResponse, HttpResponseServerError
from django.template import loader
from .models import Message, Event
from .serializers import MessageSerializer, EventSerializer
from rest_framework import generics


# Create your views here.

class MessageCreateViewSet(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageListViewSet(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class EventViewSet(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListViewSet(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def authenticate(request):
    if request.method == 'POST':
        return HttpResponse(request)
