from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth.hashers import check_password
from django.contrib import messages


# Create your views here.
def history(request):
    record = Member.objects.all()
        
    return render(
        request, 'history/history.html',
        {'data': record}
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