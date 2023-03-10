from django.shortcuts import render
from .models import Patient
from .serializers import PatientSerilizer
from rest_framework import viewsets

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerilizer