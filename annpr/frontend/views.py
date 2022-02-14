from django.shortcuts import render

from django.shortcuts import redirect, render
from .models import NumberPlate
from .forms import ModelForm1,ModelForm2
def index(request):
    numb=NumberPlate.objects.all()
    form1 = ModelForm1()  
    context={
        'numb':numb,
        'form' :form1
    }
    return render(request,'index.html',context)
def index(request):
    numb=NumberPlate.objects.all()
    form2 = ModelForm2()  
    context={
        'numb':numb,
        'form' :form2
    }
    return render(request,'index.html',context)

def add(request):
    if request.method == "POST":
        form= ModelForm2(request.POST,request.FILES) 
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