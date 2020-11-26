from rest_framework import serializers

from .models import Message, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('type', 'text')
        depth = 2

class MessageSerializer(serializers.ModelSerializer):
    event = EventSerializer(many=False)
    class Meta:
        model = Message
        depth = 2
        fields = ('token', 'event')

    def create(self, validated_data):
        event_data = validated_data.pop('event')
        events = Event.objects.create(**event_data)
        message = Message.objects.create(event=events, **validated_data)
        return message
