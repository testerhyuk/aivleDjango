from django.shortcuts import render
from .models import Member

# Create your views here.
def history(request):
    record = Member.objects.all()
        
    return render(
        request, 'history/history.html',
        {'data': record}
    )