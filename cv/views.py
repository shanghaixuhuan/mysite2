from django.shortcuts import render
from .models import BasicInformation


def cv_index(request):
    basic_info = BasicInformation.objects.all()
    return render(request, "index.html", {'basic_info': basic_info})
