from django.shortcuts import render, redirect
from member.models import Member
from history.models import History

def triceps(request):
    return render(request, 'triceps/triceps.html')

def update_count(request):
    if request.method == 'POST':
        triceps = request.POST.get('ud_count')
        t = History(triceps=triceps)
        t.save()

        member_id = request.session['member_id']
        m = History(member_id=Member.objects)
        m.save()
    return redirect('home')