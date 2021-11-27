from django.shortcuts import render
from rest_framework import viewsets
from .models import Option
from .serializers import OptionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

def home_page(request):
    return render(request,"index.html")

# Create your views here.
