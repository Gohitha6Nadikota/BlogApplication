from django import forms
from .models import Post

class Form(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag','author','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title tag'}),
            'author':forms.Select(attrs={'class':'form-control mt-2'}),
            'body':forms.Textarea(attrs={'class':'form-control mt-2','placeholder':'Enter your content'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title tag'}),
            'body':forms.Textarea(attrs={'class':'form-control mt-2','placeholder':'Enter your content'}),
        }