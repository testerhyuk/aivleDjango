from django.shortcuts import render
from .models import Member, History

# Create your views here.
def info(request):
    info = Member.objects.all()
        
    return render(
        request, 'history/history.html',
        {'info': info}
    )

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

