from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializer import CustomUserSerializer
from rest_framework.viewsets import ModelViewSet
from .models import MyModel


class Simple(ModelViewSet):
    queryset=MyModel.objects.all()
    serializer_class=CustomUserSerializer
