from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #  path('display/<int:pk>',views.displayall,name='displayall'),
    path('add/', views.add, name='add')
]
