from django.shortcuts import render
from app.models import val
from .forms import valform,CronForm
# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,'home.html',{'name':'ravi'})
def register(request):
    form=valform()
    if request.method=="POST":
        form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=valform()
        return render(request,'index.html',{'form':form})
def add(request):
    v1=int(request.GET['n1'])
    v2 = int(request.GET['n2'])
    result=v1*v2
    return render(request,'res.html',{'result':result})
def dbl(request):
    list = val.objects.values_list('id', flat=True)
    for row in list:
        query = val.objects.filter(id=row).values('v1', 'v2', 'v3')
        a = query[0]['v1']
        b = query[0]['v2']
        c = query[0]['v3']
        d=a*b
        c=d
        if c==d:
            # val.objects.filter(id=row).update(v3='haii')
            # we can use both srt & int variables
            val.objects.filter(id=row).update(v3=c)
        else:
            val.objects.filter(id=row).update(v3=c)
    message = {"message": 'data updated successfully'}
    return HttpResponse(message)
def fff(request):
    form = CronForm()
    if request.method == "POST":
        form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CronForm()
        return render(request, 'index.html', {'form': form})