from django.shortcuts import render

from custom_user.models import MyUser

def index(request):
    return render(request, "index.html")