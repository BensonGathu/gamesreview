from django import forms
from .models import Profile,Game,Review

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','link']

class GameUploadForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','description','game_type','video']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','contact']
