from django import forms
from .models import Profile,Game,Review,Answers,Forum,Query

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

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title','desc']

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = [ 'title']

class AnswersForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['answer','link']