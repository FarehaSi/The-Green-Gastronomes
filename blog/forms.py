from .models import Comment, UserProfile, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'profile_picture')


class RecipeForm(forms.ModelForm):
    instructions = forms.CharField(
        widget=SummernoteWidget())

    class Meta:
        model = Recipe
        fields = ['title', 'excerpt', 'instructions', 'featured_image']
