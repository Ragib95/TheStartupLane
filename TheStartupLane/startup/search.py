from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from models import *

# Create your search here.


def startup_by_city(request, city_name):
    startup_list = StartupName.objects.get(location=city_name)
    return render_to_response('startup/startups.html', {'startup_list': startup_list})
