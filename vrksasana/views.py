from django.shortcuts import render, redirect



# Create your views here.
def vrksasana(request):
    return render(
        request, 'vrksasana/vrksasana.html')
    
# def update_count(request):
#     if request.method == 'POST':
#         member_id = request.session['member_id']
#         vrksasana = request.POST.get('ud_count')
#         t = History
#         )