from django.shortcuts import render
from . models import Profile,Game,Review
# Create your views here.

def index(request):
    games = Game.objects.order_by("-id")
    return render(request,'index.html',{'games':games})