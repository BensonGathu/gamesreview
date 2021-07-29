from django.shortcuts import render,redirect,get_object_or_404
from . models import Profile,Game,Review,Forum,Query,Answers
from .forms import GameUploadForm,NewReviewForm,ProfileForm,ForumForm,QueryForm,AnswersForm
from embeddify import Embedder
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
           
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'registration/register.html',{"form":form})

def logoutpage(request):
    logout(request)
    return redirect('login')



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
    return render(request,'game.html',{"all_reviews":all_reviews,"form":form})

@login_required(login_url="login")
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

@login_required(login_url="login")
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


@login_required(login_url="login")
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


@login_required(login_url='login')
def join_forum(request, id):
    forum = get_object_or_404(Forum, id=id)
    request.user.profile.forum = forum
    request.user.profile.save()
    return redirect('game_forums',id)

@login_required(login_url='login')
def leave_forum(request, id):
    forum = get_object_or_404(Forum, id=id)
    request.user.profile.forum = None
    request.user.profile.save()
    return redirect('game_forums',id)

def game_forums(request,id):
    forums = Forum.get_forums(id=id)
    game = get_object_or_404(Game, id=id)
    user = request.user
    if request.method == 'POST':
        form = ForumForm(request.POST or None,request.FILES)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.game = game
            forum.user = user
            forum.save()
        return redirect('game_forums',id)
    else:
        form = ForumForm()

    return render(request,'forums.html',{"forums":forums,"game":game,"form":form})

def get_queries(request,id):
    queries = Query.objects.filter(forum=id).order_by("-id")
    forum = get_object_or_404(Forum, id=id)
    if request.method == 'POST':
        form = QueryForm(request.POST or None,request.FILES)
        if form.is_valid():
            query = form.save(commit=False)
            query.user = request.user
            query.forum = forum
            query.save()
        return redirect('game_queries',id)
    else:
        form = QueryForm()
       
    return render(request,'forum_queries.html',{"queries":queries,"form":form,"forum":forum})

# def create_query(request):
#     forum =  request.user.profile
#     form = QueryForm()
#     if request.method == 'POST':
#         form = QueryForm(request.POST or None,request.FILES)
#         if form.is_valid():
#             query = form.save(commit=False)
#             query.user = request.user
#             query.forum =  forum
#             query.save()
#         return redirect('game_forums',id)
#     else:
#         form = QueryForm()
     
#     return render(request,'createquery.html',{"form":form,"forum":forum})

def get_answers(request,id):
    all_answer = Answers.get_all_answers(id)
    query = get_object_or_404(Query, pk=id)
    forum = query.forum
    form = AnswersForm()
    if request.method == 'POST':
        form = AnswersForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.query = query
            answer.author = request.user
            answer.save()
        return HttpResponseRedirect(request.path_info)       
        # return redirect('comments')

    else:
        form = AnswersForm()
    return render(request,"replies.html",{"all_answer":all_answer,"form":form,"query":query,"forum":forum})
