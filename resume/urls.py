from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('CodeProfile', views.codeprofile, name="codeprofile"),
    path('Resume', views.resume, name="resume"),

]