from django import forms
from .models import Category, Page


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
