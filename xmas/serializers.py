from rest_framework import serializers
from .models import GuestBook, HostPost

class GuestBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestBook
        fields = '__all__'

class HostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostPost
        fields = '__all__'

                