from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,Employe
from api.serializers import companySerializer,employeSerializer

from rest_framework.response import responses
# Create your views here.
class companyViewset(viewsets.ModelViewSet):
  queryset         =company.objects.all()
  serializer_class =companySerializer


  

class employeViewset(viewsets.ModelViewSet):
  queryset         =Employe.objects.all()
  serializer_class =employeSerializer
