from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.utils import timezone

# Create your views here.


def myself(request):
    return render(request, 'MainInfo/myself.html', {})


def experience(request):
    return render(request, 'MainInfo/experience.html', {})


def education(request):
    return render(request, 'MainInfo/education.html', {})


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('thanks')
    else:
        form = FeedbackForm()
        return render(request, 'MainInfo/feedback.html', {'form': form})


def thanks(request):
    return render(request, 'MainInfo/thanks.html', {})
