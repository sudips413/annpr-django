from django.db import models

class NumberPlate(models.Model):
    number=models.CharField(max_length=15,unique=True)
    entrydate= models.DateTimeField(auto_now_add=True, auto_now=False, blank= True)
    img = models.ImageField(upload_to='images/',blank=True)
    videofile= models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.number
   