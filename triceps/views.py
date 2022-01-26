from django.shortcuts import render, redirect
from member.models import Member
from history.models import History

def triceps(request):
    return render(request, 'triceps/triceps.html')

def update_count(request):
    if request.method == 'POST':
        member_id = request.session['member_id']
        triceps = request.POST.get('ud_count')
        t = History(triceps=triceps, member_id=Member.objects.get(member_id = member_id))
        t.save()

    return redirect('home')