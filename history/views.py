from django.shortcuts import render
from .models import Member, Profile
from .forms import ProfileCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Member, History
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
    email = Member.objects.filter(member_id=request.session['member_id']).values_list('email').get()
    phone = Member.objects.filter(member_id=request.session['member_id']).values_list('phone').get()
    height = Member.objects.filter(member_id=request.session['member_id']).values_list('height').get()
    weight = Member.objects.filter(member_id=request.session['member_id']).values_list('weight').get()
    squat = History.objects.filter(member_id_id=request.session['member_id']).values_list('squat').filter()
    
    context = {'email':email, 'phone':phone, 'height':height, 'weight':weight, 'squat':squat}
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


        