from django.http import HttpResponse, request
from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone



# Create your views here.
#def index(request):
#    return render(request, 'index.html')
#def leaderboard(request):
#    return render(request, 'leaderboard.html')
def practice(request):
    return render(request, 'PracticePage.html')