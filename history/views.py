from django.shortcuts import render, redirect
from .models import Member, History
from django.contrib import messages


# Create your views here.
def info(request):
    info = Member.objects.all()
        
    return render(
        request, 'history/history.html',
        {'data': info}
    )

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
        # for i in m:
        #     if m[i].member_id == request.session['member_id']:
        #         m.delete()
        #         request.session.flush()
        #         return redirect('home')
        # m = request.m
        # if check_password(pw_del, m.psw_rg):
        #     m.delete()
        # return redirect('home')
    else:
        return render(request, 'history/member_del.html')

def history(request):
    email = Member.objects.filter(member_id=request.session['member_id']).values_list('email').get()
    phone = Member.objects.filter(member_id=request.session['member_id']).values_list('phone').get()
    height = Member.objects.filter(member_id=request.session['member_id']).values_list('height').get()
    weight = Member.objects.filter(member_id=request.session['member_id']).values_list('weight').get()
    context = {'email':email, 'phone':phone, 'height':height, 'weight':weight}
    return render(
        request,
        'history/history.html',
        context
    )