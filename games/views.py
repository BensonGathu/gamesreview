from django.shortcuts import render
from . models import Profile,Game,Review
# Create your views here.

def index(request):
    games = Game.objects.order_by("-id")
    return render(request,'index.html',{'games':games})


def reviews(request,id):
    all_reviews = Review.get_reviews(id)
    game = get_object_or_404(Game,pk=id)

    form = NewReviewForm()
    if request.method == 'POST':
        form = NewReviewForm(request.POST)
        if form.is_valid()
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = NewReviewForm()
    return render(request,'reviews.html',{"all_reviews":all_reviews,"form":form})


def singlegame(request,id):
    game = Game.objects.get(id=id)

    return render(request,'game.html',{"game":game})

def profile(request):
    pass

def upload_game(request):
    pass

def search_game(request):
    pass