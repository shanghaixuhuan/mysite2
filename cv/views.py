from django.shortcuts import render
from .models import BasicInformation, Education


def cv_index(request):
    basic_infos = BasicInformation.objects.all()
    educations = Education.objects.all()
    return render(request, "index.html", {'basic_infos': basic_infos,
                                          'educations': educations})
