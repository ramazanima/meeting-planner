from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")
def message(request):
    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})
