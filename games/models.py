from django.db import models
from django.contrib.auth.models import User
# from embeddify import Embedder
from embed_video.fields import EmbedVideoField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='images/',default='SOME IMAGE')
    bio = models.CharField(max_length=250)
    contact = models.IntegerField(null=True)
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
