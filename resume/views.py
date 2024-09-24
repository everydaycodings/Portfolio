from lib2to3.fixes.fix_input import context

from decouple import config
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from storages.utils import setting

from .models import StaticAssets, OpenSource, Competitive, Education, Experience, Skill, Extra
from .forms import ContactUsForm
# Create your views here.
def index(request):

    profile = get_object_or_404(StaticAssets, reference_name="profile")
    tag1value = get_object_or_404(StaticAssets, reference_name="tag1value")
    tag2value = get_object_or_404(StaticAssets, reference_name="tag2value")
    tag3value = get_object_or_404(StaticAssets, reference_name="tag3value")
    tag4value = get_object_or_404(StaticAssets, reference_name="tag4value")
    profession = get_object_or_404(StaticAssets, reference_name="profession")
    bio = get_object_or_404(StaticAssets, reference_name="index_bio")
    twitter = get_object_or_404(StaticAssets, reference_name="twitter")
    linkedin = get_object_or_404(StaticAssets, reference_name="linkedin")
    github = get_object_or_404(StaticAssets, reference_name="github")
    tag1 = get_object_or_404(StaticAssets, reference_name="tag1")
    tag2 = get_object_or_404(StaticAssets, reference_name="tag2")
    tag3 = get_object_or_404(StaticAssets, reference_name="tag3")
    tag4 = get_object_or_404(StaticAssets, reference_name="tag4")
    resume = get_object_or_404(StaticAssets, reference_name="resume")

    context = {
        "profile": profile,
        "profession": profession,
        "bio": bio,
        "resume": resume,
        "twitter": twitter,
        "linkedin": linkedin,
        "github": github,
        "tag1": tag1,
        "tag2": tag2,
        "tag3": tag3,
        "tag4": tag4,
        "tag1value": tag1value,
        "tag2value": tag2value,
        "tag3value": tag3value,
        "tag4value": tag4value,
    }

    return render(request, "index.html", context=context)


def codeprofile(request):

    open_sources = OpenSource.objects.all()
    competitive = Competitive.objects.all().order_by('-id')

    context = {
        "open_sources": open_sources,
        "competitive": competitive,
        "media_url": settings.MEDIA_URL,
    }

    return render(request, "code_profile.html", context=context)


def resume(request):

    educations = Education.objects.all().order_by('-id')
    experiences = Experience.objects.all().order_by('-id')
    skills = Skill.objects.all().order_by('id')
    aboutme = get_object_or_404(Extra, reference="aboutme")

    whyhireme = get_object_or_404(Extra, reference="whyhireme")
    myeducationdesc = get_object_or_404(Extra, reference="myeducationdesc")
    myexperiencedesc = get_object_or_404(Extra, reference="myexperiencedesc")
    myskillsdesc = get_object_or_404(Extra, reference="myskillsdesc")
    aboutmedesc = get_object_or_404(Extra, reference="aboutmedesc")

    context = {
        "educations": educations,
        "experiences": experiences,
        "skills": skills,
        "aboutme": aboutme,
        "whyhireme": whyhireme,
        "myeducationdesc": myeducationdesc,
        "myexperiencedesc": myexperiencedesc,
        "myskillsdesc": myskillsdesc,
        "aboutmedesc": aboutmedesc,
    }

    return render(request, "resume.html", context=context)


def contactsuccess(request):
    return render(request, "contact_success.html")

def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('contact_success')

    email1 = get_object_or_404(StaticAssets, reference_name="email1")
    email2 = get_object_or_404(StaticAssets, reference_name="email2")
    linkedin = get_object_or_404(StaticAssets, reference_name="linkedin")
    twitter = get_object_or_404(StaticAssets, reference_name="twitter")

    context = {
        "email1": email1,
        "email2": email2,
        "linkdin": linkedin,
        "twitter": twitter,
    }

    return render(request, "contact.html", context=context)