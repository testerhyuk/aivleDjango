from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Member
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        email = request.POST.get('email')
        member_name = request.POST.get('member_name')
        psw_rg = request.POST.get('psw_rg')
        phone = request.POST.get('phone')
        height = request.POST.get('height')
        weight = request.POST.get('weight')

        m = Member(
            member_id=member_id,
            email=email,
            member_name=member_name, 
            psw_rg=psw_rg,
            phone=phone,
            height=height,
            weight=weight
        )
        m.save()

        return redirect('home')
    else:
        return redirect('home')


def login(request):
    if request.method == 'POST':
        memberid = request.POST.get('memberid')
        pswrg = request.POST.get('pswrg')

        try:
            m = Member.objects.get(memberid=memberid, pswrg=pswrg)
        except:
            messages.info(request, '아이디 또는 비밀번호가 틀렸습니다.')
            

        return redirect('home')
    else:
        return redirect('home')