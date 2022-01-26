from django.shortcuts import redirect, render
from history.models import History
from member.models import Member

def shoulder(request):
    return render(request, 'shoulder/shoulder.html')

def update_count(request):
    if request.method == 'POST':
        shoulder = request.POST.get('ud_count')
        print(shoulder)
        t = History(shoulder=shoulder)
        t.save()

        member_id = request.session['member_id']
        m = History(member_id=Member.objects)
        m.save()
    return redirect('home')