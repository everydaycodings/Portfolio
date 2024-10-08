import os
from lib2to3.fixes.fix_input import context
from dotenv import load_dotenv
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from storages.utils import setting
from django.core.mail import send_mail
from .models import StaticAssets, OpenSource, Competitive, Education, Experience, Skill, Extra
from django.views.decorators.cache import cache_page
from .forms import ContactUsForm

load_dotenv()

cache_time = 60 * int(os.getenv('CACHE_TIME'))

# Create your views here.
@cache_page(60 * cache_time)
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

@cache_page(60 * cache_time)
def codeprofile(request):

    open_sources = OpenSource.objects.filter(published=True)
    competitive = Competitive.objects.all().order_by('-id')

    context = {
        "open_sources": open_sources,
        "competitive": competitive,
        "media_url": settings.MEDIA_URL,
    }

    return render(request, "code_profile.html", context=context)

@cache_page(60 * cache_time)
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

@cache_page(60 * cache_time)
def contactsuccess(request):
    return render(request, "contact_success.html")


@cache_page(60 * cache_time)
def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()

            message_content = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('email')
            send_mail(
                subject = "New Message Form Portfolio",
                message = f"""
                                A Message Has been sent By: {sender}
                                
                                {message_content}
    
                            """,
                from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list = [settings.ADMIN_EMAIL1, settings.ADMIN_EMAIL2],
                fail_silently = True,
            )

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


@cache_page(60 * cache_time)
def article(request):
    return render(request, "articles.html")