from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TeamForm
from .models import Profile, Player, Team 
# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'dashboard/team_detail.html')
    
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def create_team(request):
    team_form = TeamForm()
    return render(request, 'dashboard/team_detail.html',{
        'team_form':team_form,
    })

def add_team(request):
    form = TeamForm(request.POST)
    if form.is_valid():
        new_team=form.save(commit=False)
        model2 = Profile.objects.get(user_id=request.user.id)
        model2.team = new_team.id

        new_team.save()
        model2.save()
        print("ypoooooooooooooxxxxxxxxxxxxxo", model2)

    return redirect('detail')
        
    # model = Team 
    # fields = ['team_name']
        

class DreamUpdate(UpdateView):
    model = Team
    fields='__all__'

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            model = Profile.objects.create()
            model.user=user
            model.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up-Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message':error_message}
    return render(request, 'registration/signup.html', context)
