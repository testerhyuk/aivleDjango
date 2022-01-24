from django.shortcuts import render

# Create your views here.

def pullup(request):
    return render(request, 'pullup/pullup.html')