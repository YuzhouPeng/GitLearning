from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import Http404

from django.http import HttpResponse




def index(request):
    return render(request, 'citymanage/index.html')
def about(request):
    return render(request, 'citymanage/about.html')
def station(request):
    return render(request, 'citymanage/station.html')
def emission(request):
    return render(request, 'citymanage/emission.html')