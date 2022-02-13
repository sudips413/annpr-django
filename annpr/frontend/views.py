from django.shortcuts import render

from django.shortcuts import redirect, render
from .models import NumberPlate
from .forms import ModelForm
def index(request):
    numb=NumberPlate.objects.all()
    form = ModelForm()
    context={
        'numb':numb,
        'form' :form
    }
    return render(request,'index.html',context)

def add(request):
    if request.method == "POST":
        form= ModelForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
    return redirect('/')

# def display(request):
#     if request.method == "POST":
#         numb=NumberPlate.objects.all()
#         form = ModelForm(request.POST)
#         context={
#             'numb':numb,
#             'form' :form
#     }
#     return render(request,'index.html',context)