# from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

# def home(request):
#     return HttpResponse("Hello, Shezan Mahmud.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer