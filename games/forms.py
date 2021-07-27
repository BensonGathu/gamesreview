from django import forms
from .models import Profile,Game,Review

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','link']

class GameUploadForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','trailer_link','game_type','description']
