from django.shortcuts import render

def triceps(request):
    return render(request, 'triceps/triceps.html')