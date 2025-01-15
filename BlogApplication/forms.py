from django import forms
from .models import Post,Category

catags=Category.objects.all().values_list('name','name')
catags_list=[]

for x in catags:
    catags_list.append(x)
class Form(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag','author','category','body','snippet')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title tag'}),
            'author':forms.TextInput(attrs={'class':'form-control mt-2','id':'Authorname','value':'','disabled':'disabled'}),
            'category':forms.Select(choices=catags_list,attrs={'class':'form-control mt-2'}),
            'body':forms.Textarea(attrs={'class':'form-control mt-2','placeholder':'Enter your content'}),
            'snippet':forms.Textarea(attrs={'class':'form-control mt-2'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag','body','snippet')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control mt-2','placeholder':'Enter your title tag'}),
            'body':forms.Textarea(attrs={'class':'form-control mt-2','placeholder':'Enter your content'}),
            'snippet':forms.Textarea(attrs={'class':'form-control mt-2','placeholder':'Enter the snippet content'})
        }