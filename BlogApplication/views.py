from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import Form,EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-postDate']

class DetailsView(DetailView):
    model=Post
    template_name='details.html'

class CreatePostView(CreateView):
    model=Post
    form_class=Form
    template_name='create.html'

class EditPostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='edit.html'

class DeletePostView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('home')

    