from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GuestBookSerializer, HostPostSerializer
from .models import GuestBook, HostPost

class GuestBookView(viewsets.ModelViewSet):
    serializer_class = GuestBookSerializer
    queryset = GuestBook.objects.all()

class HostPostView(viewsets.ModelViewSet):
    serializer_class = HostPostSerializer
    queryset = HostPost.objects.all()    