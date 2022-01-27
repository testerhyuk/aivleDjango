from .models import Member, Profile, History
from .forms import ProfileCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime

def member_del(request):
    if request.method == "POST":
        pw_del = request.POST["pw_del"]
        m = Member.objects.filter(psw_rg=pw_del)

        try:
            m = Member.objects.get(member_id=request.session['member_id'], psw_rg=pw_del)
        except:
            msg = '비밀번호가 틀렸습니다.'
            return render(request, 'history/member_del.html', { 'msg': msg })
        else:
            m.delete()
            request.session.flush()
            return redirect('home')
    else:
        return render(request, 'history/member_del.html')

def history(request):
    member = Member.objects.get(member_id=request.session['member_id'])
    email = member.email
    phone = member.phone
    height = member.height
    weight = member.weight

    try:
        uploadFile = Profile.objects.get(member=member)
    except:
        uploadFile = ''

    triceps = History.objects.filter(member_id_id=request.session['member_id']).values_list('triceps', flat=True).filter(date=datetime.today())
    shoulder = History.objects.filter(member_id_id=request.session['member_id']).values_list('shoulder', flat=True).filter(date=datetime.today())
    squat = History.objects.filter(member_id_id=request.session['member_id']).values_list('squat', flat=True).filter(date=datetime.today())
    pullup = History.objects.filter(member_id_id=request.session['member_id']).values_list('pullup', flat=True).filter(date=datetime.today())
    vrksasana = History.objects.filter(member_id_id=request.session['member_id']).values_list('vrksasana', flat=True).filter(date=datetime.today())

    triceps = sum(triceps)
    shoulder = sum(shoulder)
    squat = sum(squat)
    pullup = sum(pullup)
    vrksasana = sum(vrksasana)
    
    context = {'email':email, 'phone':phone, 'height':height, 'weight':weight, 'uploadFile':uploadFile,
        'triceps':triceps, 'shoulder':shoulder, 'squat':squat, 'pullup':pullup, 'vrksasana':vrksasana}
    return render(
        request,
        'history/history.html',
        context
    )

def change_image(request):
    return render(
        request,
        'history/change_image.html'
    )

def upload(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            member = Member.objects.get(member_id=request.session['member_id'])
            profile.member = member
            profile.save()
        else:
            form = ProfileCreationForm()
    return render(
        request, 
        'history/change_image.html',
        {'form': form}
    )