from lib2to3.fixes.fix_input import context

from decouple import config
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import StaticAssets
# Create your views here.
def index(request):

    profile = get_object_or_404(StaticAssets, reference_name="profile")
    experience = get_object_or_404(StaticAssets, reference_name="years_experience")
    projects = get_object_or_404(StaticAssets, reference_name="projects_completed")
    tech = get_object_or_404(StaticAssets, reference_name="known_tech")
    commits = get_object_or_404(StaticAssets, reference_name="code_commits")
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
        "experience": experience,
        "projects": projects,
        "tech": tech,
        "commits": commits,
        "profession": profession,
        "bio": bio,
        "twitter": twitter,
        "linkedin": linkedin,
        "github": github,
        "tag1": tag1,
        "tag2": tag2,
        "tag3": tag3,
        "tag4": tag4,
        "resume": resume,
    }

    return render(request, "index.html", context=context)