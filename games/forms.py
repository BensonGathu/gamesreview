from django import forms
from .models import Profile,Game,Review

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','link']

class GameUploadForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','video','game_type','description']
