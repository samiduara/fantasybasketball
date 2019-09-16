from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile, Player
# Create your views here.

def home(request):
    return render(request, 'home.html')
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

class DreamCreate(CreateView):
    model = Player
    fields = '__all__'

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up-Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message':error_message}
    return render(request, 'registration/signup.html', context)
