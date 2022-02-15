from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import NumberPlate, Image, Video
from .forms import ModelForm1,ImageForm, VideoForm


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def get_image(request):
    numb=NumberPlate.objects.all()
    form = ImageForm()  
    context={
        'numb':numb,
        'form': form,
        'title': 'Image'
    }
    return render(request,'upload_form.html',context)

def get_video(request):
    numb=NumberPlate.objects.all()
    form = VideoForm()  
    context={
        'numb':numb,
        'form': form,
        'title': 'Video'
    }
    return render(request,'upload_form.html',context)

def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        file = request.FILES.get('img')
        filename = file.name
        print(filename)
        print(file)
        if form.is_valid():
            form.save()
            return redirect('display_image')
    else:
        return redirect('get_image')
    

def upload_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST,request.FILES)
        file = request.FILES.get('videofile')
        filename = file.name
        if filename.endswith('.mp4') or filename.endswith('.avi'):
            print('File is a video')
            if form.is_valid():
                form.save()
                return redirect('display_video')
        else:
            print('File not a video')
            return redirect('get_video')
    else:
        return redirect('get_video')

def display_image(request):
    latest_image = Image.objects.latest('id');
    number_plate = NumberPlate.objects.all();
    image = latest_image.img
    context = {
        'image': image,
        'number_plate': number_plate
    }
    return render(request, 'detections/image.html',context)

def display_video(request):
    return render(request,'detections/video.html')
