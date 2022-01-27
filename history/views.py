from django.shortcuts import render
from .models import Member, Profile
from .forms import ProfileCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
# def info(request):
#     info = Member.objects.all()
        
#     return render(
#         request, 'history/history.html',
#         {'info': info}
#     )

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