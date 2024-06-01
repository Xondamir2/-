from django.shortcuts import render
from rest_framework import generics
from .models import Hudud, QurilishTashkiloti, QuriishBinosi
from .serializer import HududSerializer,QurilishBinosiSerializer,QurilishTashkilotiSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class QurilishTashkilotiAPIList(generics.ListCreateAPIView):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer

class QurilishTashkilotiAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class QurilishTashkilotiAPICreate(generics.CreateAPIView):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer

class QurilishTashkilotiAPIUpdate(generics.UpdateAPIView):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer



class HududAPIList(generics.ListCreateAPIView):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer

class HududAPIDetail(generics.RetrieveAPIView):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer


class HududAPICreate(generics.CreateAPIView):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer

class HududAPIUpdate(generics.UpdateAPIView):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer


class QurilishBinosiAPIList(generics.ListCreateAPIView):
    queryset = QuriishBinosi.objects.all()
    serializer_class = QurilishBinosiSerializer


class QurilishBinosiAPIDetail(generics.RetrieveAPIView):
    queryset = QuriishBinosi.objects.all()
    serializer_class = QurilishBinosiSerializer


class QurilishBinosiAPICreate(generics.CreateAPIView):
    queryset = QuriishBinosi.objects.all()
    serializer_class = QurilishBinosiSerializer


class QurilishBinosiAPIUpdate(generics.UpdateAPIView):
    queryset = QuriishBinosi.objects.all()
    serializer_class = QurilishBinosiSerializer
