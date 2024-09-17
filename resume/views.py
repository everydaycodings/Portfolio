from lib2to3.fixes.fix_input import context

from decouple import config
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import StaticAssets
# Create your views here.
def index(request):

    profile = get_object_or_404(StaticAssets, reference_name="profile")

    context = {
        "profile": profile
    }

    return render(request, "index.html", context=context)