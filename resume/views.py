from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
def index(request):
    return render(request, "index.html")