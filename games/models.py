from django.db import models
from django.contrib.auth.models import User
# from embeddify import Embedder
from embed_video.fields import EmbedVideoField

# Create your models here.

class Game(models.Model):
    GAME_TYPE = (
    ("Action" , "Action"),
    ("Adventure", "Adventure"),
    ("Role-playing", "Role-playing"),
    ("Simulation", "Simulation"),
    ("Strategy", "Strategy"),
    ("Sports", "Sports"),
    ("Puzzle", "Puzzle"),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    game_type = models.CharField(max_length=250,choices=GAME_TYPE,default="Select type of game")
    video = EmbedVideoField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def save_game(self):
        self.save()

    def delete_game(self):
        self.delete()
    @classmethod
    def search_game(cls,title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def convert_link(cls,trailer_link):
        embedder = Embedder()
        return embedder(trailer_link)

class Forum(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE,related_name="forum")
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_forum(self):
        self.save()
    def __str__(self):
        return self.title
    
    @classmethod
    def get_forums(cls,id):
        return cls.objects.filter(game=id).all()


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='images/',default='SOME IMAGE')
    bio = models.CharField(max_length=250)
    contact = models.IntegerField(null=True)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE, related_name='user_forum',null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    # @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
    # def save_profile(sender, instance, created, **kwargs):
    #     user = instance
    #     if created:
    #         profile = Profile(user=user)
    #         profile.save()
    

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    game = models.ForeignKey(Game,on_delete=models.CASCADE,related_name="reviews")
    date_created = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=250,blank=True)

    def save_review(self):
        self.save()
        
    def __str__(self):
        return self.review
    def delete_review(self):
        self.delete()
    
    @classmethod
    def get_reviews(cls,game_id):
        return cls.objects.filter(game=game_id).all()



class Query(models.Model):
    title = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name="query_forum")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_query(self):
        self.save()
    def __str__(self):
        return self.title

class Answers(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    query = models.ForeignKey(Query,on_delete=models.CASCADE,related_name="answers")
    link = models.URLField(max_length=250,blank=True)

    def save_answer(self):
        self.save()
        
    def __str__(self):
        return self.answer
    def delete_answer(self):
        self.delete()
    
    @classmethod
    def get_all_answers(cls,query_id):
        return cls.objects.filter(query=query_id).all()



