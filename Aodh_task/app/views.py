from django.shortcuts import render,redirect
from django.urls import reverse_lazy
import pdb;
pdb.set_trace()
from app.forms import healthform
# Create your views here.
from django.http import HttpResponse
from app.models import helth
from django.views.generic import UpdateView
def helth_view(request):
    # if request.method == 'POST':
    #     form = healthform(request.POST)
    #     if form.is_valid():
        #     heartbeat=0
        #     himoglobin=0
        #     breathingrate=0
        #     if heartbeat<=70 and himoglobin<=60 and breathingrate<=10:
        #         print('he will die with in 7 days')
        #         # return  render('home.html')
    #         form.save()
    #     # else:
    #     #     print('not valid')
    # else:
    #     form=healthform()
    #     return render(request,'helth.html',{'form':form})
    if request.method=='POST':
        pdb.set_trace()
        form=healthform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=healthform
    return render(request,'helth.html',{'form':form})
def health_check(request):
    form=healthform()
    if request.method=="POST":
        if form.is_valid():
            h=form.cleaned_data['heartbeat']
            hmn=form.cleaned_data['himoglobin']
            br=form.cleaned_data['breathingrate']
            if h < 70 and hmn < 60 and br < 10:
                return HttpResponse('will die with in 7 days')
            else:
                return HttpResponse('not die')
            result = helth.objects.all()
            # heartbeat = h, himoglobin = hmn, breathingrate = br
            result.save()
        else:
            form.errors
    else:
        form=helth.objects.all()
        return render(request,'display.html',{'form':form})
def display(request):
    data=helth.objects.all()
    return render(request,'display.html',{'data':data})
# def update(request, id):
#     data = helth.objects.get(id=id)
#     return render(request,'edit.html',{'data':data})
class update_view(UpdateView):
    model = helth
    fields = '__all__'
    success_url = reverse_lazy('helth-update')

def check(request):
    form = healthform()
    if request.method == "POST":
        if form.is_valid():
            h = form.cleaned_data['heartbeat']
            hmn = form.cleaned_data['himoglobin']
            br = form.cleaned_data['breathingrate']
            result = helth.objects.filter(h=h, hmn=hmn, br=br)
            if h<70 and hmn<60 and br<10:
                return HttpResponse('will die within 7 days')
            else:
                return  render('/home')
            result.save()
    return render(request,'home.html')