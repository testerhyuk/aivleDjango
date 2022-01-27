from django.shortcuts import render
from .models import Member, History

# Create your views here.
def info(request):
    info = Member.objects.all()
        
    return render(
        request, 'history/history.html',
        {'info': info}
    )

def history(request):
    record = History.objects.all()
        
    return render(
        request, 'history/history.html',
        {'record': record}
    )