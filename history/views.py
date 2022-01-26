from django.shortcuts import render

# Create your views here.
def history(request):
    return render(
        request, 'history/history.html')