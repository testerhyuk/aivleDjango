from .models import Member, Profile
from .forms import ProfileCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

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
        print(uploadFile)
    except:
        uploadFile = ''
    context = {'email':email, 'phone':phone, 'height':height, 'weight':weight, 'uploadFile':uploadFile}

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

def img_show(request):
    id = request.GET.get('id')
    uploadFile = Profile.objects.get(id=id)
    return render(
        request, 'history/history.html',
        {'uploadFile': uploadFile})