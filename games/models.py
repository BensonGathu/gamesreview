from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='images/',default='SOME IMAGE')
    bio = models.CharField(max_length=250)
    contact = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

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
    trailer_link = models.URLField(max_length=250)
    game_type = models.CharField(max_length=250,choices=GAME_TYPE,default="Select type of game")
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

    

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    game = models.ForeignKey(Game,on_delete=models.CASCADE,related_name="reviews")
    date_created = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=250,null=True)

    def save_review(self):
        self.save()
        
    def __str__(self):
        return self.review
    def delete_review(self):
        self.delete()
    
    @classmethod
    def get_reviews(cls,game_id):
        return cls.objects.filter(game=game_id).all()
