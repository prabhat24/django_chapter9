from django import forms
from .models import Category, Page, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=120)
    url = forms.URLField()
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta():
        model = Page
        exclude = ('category',)


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profile_website', 'profile_image',)
