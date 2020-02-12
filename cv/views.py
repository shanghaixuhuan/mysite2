from django.shortcuts import render
from .models import BasicInformation, Experience


def cv_index(request):
    basic_infos = BasicInformation.objects.all()
    experiences = Experience.objects.all()
    return render(request, "index.html", {'basic_infos': basic_infos,
                                          'experiences': experiences})
