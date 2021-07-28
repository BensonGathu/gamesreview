from django.shortcuts import render,redirect,get_object_or_404
from . models import Profile,Game,Review
from .forms import GameUploadForm,NewReviewForm,ProfileForm
from embeddify import Embedder
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    
    games = Game.objects.order_by("-id")
    # for game in games:
    #     link = Game.convert_link(game.trailer_link)
    return render(request,'index.html',{'games':games,})


def reviews(request,id):
    all_reviews = Review.get_reviews(id)
    game = get_object_or_404(Game,pk=id)

    form = NewReviewForm()
    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = NewReviewForm()
    return render(request,'reviews.html',{"all_reviews":all_reviews,"form":form})


def singlegame(request,id):
    all_reviews = Review.get_reviews(id)
    game = get_object_or_404(Game,pk=id)

    form = NewReviewForm()
    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = NewReviewForm()

    return render(request,'game.html',{"game":game,"all_reviews":all_reviews,"form":form})

def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            redirect(request.path_info)
    else:
        form = ProfileForm(instance=request.user.profile)
    profile = Profile.objects.filter(user=user)
    games = Game.objects.filter(user=user)
    return render(request,'profile.html',{"user":user,"profile":profile,"games":games,"form":form})


def upload_game(request):
    current_user = request.user
    if request.method == 'POST':
        form = GameUploadForm(request.POST or None,request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = current_user
            game.save()
        return redirect('index')
    else:
        form = GameUploadForm()
    return render(request,'gameform.html',{"form":form})
def search_game(request):
    if 'game' in request.GET and request.GET['game']:
        search_game = request.GET.get('game')
        searched_game = Game.search_game(search_game)
        message = f'{search_game}'

        return render(request,'results.html',{"message":message,"searched_game":searched_game})

    else:
        message = "Search a game"
        return render(request,'results.html',{"message":message})

