from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category
from .forms import Form,EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-postDate']

    def get_context_data(self,*args, **kwargs):
        category_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        context["category_menu"]=category_menu
        return context

class DetailsView(DetailView):
    model=Post
    template_name='details.html'

    def get_context_data(self,*args, **kwargs):
        category_menu=Category.objects.all()
        context=super(DetailsView,self).get_context_data(*args,**kwargs)
        context["category_menu"]=category_menu
        return context


class CreatePostView(CreateView):
    model=Post
    form_class=Form
    template_name='create.html'

    def get_context_data(self,*args, **kwargs):
        category_menu=Category.objects.all()
        context=super(CreatePostView,self).get_context_data(*args,**kwargs)
        context["category_menu"]=category_menu
        return context

class EditPostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='edit.html'

    def get_context_data(self,*args, **kwargs):
        category_menu=Category.objects.all()
        context=super(EditPostView,self).get_context_data(*args,**kwargs)
        context["category_menu"]=category_menu
        return context

class DeletePostView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('home')

    def get_context_data(self,*args, **kwargs):
        category_menu=Category.objects.all()
        context=super(DeletePostView,self).get_context_data(*args,**kwargs)
        context["category_menu"]=category_menu
        return context

class CreateCategoryView(CreateView):
    model=Category
    fields='__all__'
    template_name='create_category.html'  

    def get_context_data(self,*args, **kwargs):
        category_menu=Category.objects.all()
        context=super(CreateCategoryView,self).get_context_data(*args,**kwargs)
        context["category_menu"]=category_menu
        return context

def CategoryView(request,catags):
    category_posts=Post.objects.filter(category=catags.replace('-',' '))
    return render(request,'category.html',{'catags':catags.title().replace('-',' '),'category_posts':category_posts})

    