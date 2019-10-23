from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import student
from .forms import student_form
def home(request):
    return render(request,'home.html')
def student_view(request):
    list=student.objects.values_list('id',flat=True)
    for row in list:
        query=student.objects.filter(id=row).values('sb1','sb2','sb3')
        a=query[0]['sb1']
        b=query[0]['sb2']
        c = query[0]['sb3']
        if a<70 and b<60 and c<10:
            student.objects.filter(id=row).update(total='die')
        else:
            student.objects.filter(id=row).update(total='safe')
    message = {"message": 'data updated successfully'}
    return HttpResponse(message)

