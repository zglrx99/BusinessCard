from django.shortcuts import render

# Create your views here.

def main_info(request):
    return render(request, 'MainInfo/main_info.html', {})