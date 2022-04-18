from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from mainbase.models import MainBase
from mainbase.serializers import MainBaseSerializer

def main_page(request):
    return render(request, 'index.html', {'main_pages': MainBase.objects.all()})

class MainPageView(ModelViewSet):
    queryset = MainBase.objects.all()
    serializer_class = MainBaseSerializer


