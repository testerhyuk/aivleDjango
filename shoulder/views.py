from django.shortcuts import redirect, render
from history.models import History
from member.models import Member

def shoulder(request):
    return render(request, 'shoulder/shoulder.html')

def update_count(request):
    if request.method == 'POST':
        member_id = request.session['member_id']
        shoulder = request.POST.get('ud_count')
        t = History(shoulder=shoulder, member_id=Member.objects.get(member_id = member_id))
        t.save()
    return redirect('home')