from rest_framework import serializers
from .models import Push_event, Pull_request, Merge_event

class Push_event_serializer(serializers.ModelSerializer):
    class Meta:
        model=Push_event
        fields=['author', 'branch', 'datetime']

class Pull_request_serializer(serializers.ModelSerializer):
    class Meta:
        model=Pull_request
        fields=['author', 'from_branch', 'to_branch', 'datetime']

class Merge_event_serializer(serializers.ModelSerializer):
    class Meta:
        model=Merge_event
        fields=['author', 'from_branch', 'to_branch', 'datetime']