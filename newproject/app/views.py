from django.shortcuts import render
from .models import Course

# Create your views here.
def home(request):
    data=Course.objects.all()
    return render(request,'home.html',{'data':data})
