from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexfunc(repuest):
  return render(repuest,'index.html')

def listfunc(request):
  return render(request,'list_chat.html')
