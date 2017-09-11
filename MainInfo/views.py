from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.

def myself(request):
    return render(request, 'MainInfo/myself.html', {})

def experience(request):
    return render(request, 'MainInfo/experience.html', {})

def education(request):
    return render(request, 'MainInfo/education.html', {})

def feedback(request):
    form = FeedbackForm()
    return render(request, 'MainInfo/feedback.html', {'form': form})