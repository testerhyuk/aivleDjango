from django.shortcuts import render

# Create your views here.
def vrksasana(request):
    return render(
        request, 'vrksasana/vrksasana.html')