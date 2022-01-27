from django.shortcuts import render
from .models import Member, Profile
from .forms import ProfileCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Member, History
from django.contrib import messages


# Create your views here.
# def info(request):
#     info = Member.objects.all()
        
#     return render(
#         request, 'history/history.html',
#         {'info': info}
#     )
    return render(
        request, 'history/history.html',
        {'data': record}
    )

def member_del(request):
    if request.method == "POST":
        pw_del = request.POST["pw_del"]
        m = Member.objects.filter(psw_rg=pw_del)

    context = {'email':email, 'phone':phone, 'height':height, 'weight':weight}

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

# class profile_create(CreateView):
#     model = Profile
#     context_object_name = 'target_profile'
#     form_class = ProfileCreationForm
#     success_url = reverse_lazy('history:history')
#     template_name = 'history/change_image.html'

# def profile_create(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#         uploadFile = form.save()
#         # uploadFile = form.save(commit=False)
#         name = uploadFile.file.name
#         size = uploadFile.file.size
#         return HttpResponse('%s<br>%s' % (name, size))
#         else:
#         form = UploadFileForm()
#         return render(
#         request, 'file/upload3.html', {'form': form})
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
