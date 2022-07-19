from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .form import SignUpForm

from .models import Person


def index(request):
    return render(request, 'chat/index.html')

@login_required
def home(request):
    return render(request, 'chat/room.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            person = Person(user=userform)
            userform.save()
            person.save()
            return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})