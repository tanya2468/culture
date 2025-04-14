from django import forms
from .models import Indian

class IndianForm(forms.ModelForm):
    class Meta:
        model = Indian
        fields = ['title', 'image1', 'image2', 'category', 'content1', 'content2', 'content3', 'content4', 'link']
