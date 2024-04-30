from django.shortcuts import render, HttpResponse
from .forms import SkillSearchForm
from .models import Profile

# Create your views here.
def index(request):
    context = {}
    return render(request, 'portfolio/pages/index.html', context=context)
    # render function still returns httpresponse in background. views need to return response or exception!

def details(request):
    context = {}
    return render(request, 'portfolio/pages/portfolio-details.html', context=context)

def django_filters(request):
    context = {'number': 10}
    return render(request, 'filter.html', context=context)

def search_results(request):
    if request.method == 'GET':
        form = SkillSearchForm(request.GET)
        if form.is_valid():
            skill = form.cleaned_data['skill']
            print("searching for skill:", skill)
    return render(request, 'portfolio/pages/index.html', {'form': form})

def show_profile(request):
    profile = Profile.objects.filter(id=1)
    context = {'profile': profile}
    return render(request, 'portfolio/pages/profile.html', context)