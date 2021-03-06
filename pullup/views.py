from django.shortcuts import render, redirect
from member.models import Member
from history.models import History

# Create your views here.

def pullup(request):
    return render(request, 'pullup/pullup.html')

def update_count(request):
    if request.method == 'POST':
        member_id = request.session['member_id']
        pullup = request.POST.get('ud_count')
        t = History(pullup=pullup, member_id=Member.objects.get(member_id = member_id))
        t.save()

    return redirect('home')