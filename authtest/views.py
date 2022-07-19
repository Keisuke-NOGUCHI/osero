from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import Person

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html')

@login_required
def private_page(request):
    if request.method == "POST":
        p = request.user.userinfo
        p.age = request.POST["age"]
        p.username = request.POST["username"]
        p.save()
    return render(request, 'authtest/private.html', {})

def public_page(request):
    return render(request, 'authtest/public.html', {})