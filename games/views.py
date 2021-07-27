from django.shortcuts import render

# Create your views here.

def index(request):
    game = "Games"
    return render(request,'index.html',{'game':game})