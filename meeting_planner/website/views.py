from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting
from datetime import datetime

def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meeting": Meeting.objects.count()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))
def creator(request):
    return render(request, "website/creator.html")