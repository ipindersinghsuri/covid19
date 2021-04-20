from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Hospital
from django.shortcuts import render


def index(request):
    hospital_list = Hospital.objects.all()
    return render(request, "communityhelp/index.html", {"hospital_list": hospital_list})
