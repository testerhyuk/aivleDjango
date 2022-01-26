from django.shortcuts import render, redirect
from member.models import Member
from history.models import History


# Create your views here.
def vrksasana(request):
    return render(request, 'vrksasana/vrksasana.html')
    
def update_count(request):
    if request.method == 'POST':
        member_id = request.session['member_id']
        vrksasana = request.POST.get('ud_count')
        t = History(vrksasana=vrksasana, member_id = Member.objects.get(member_id = member_id))
        t.save()

    return redirect('home')