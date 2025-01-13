from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category
from .forms import Form,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

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

        getInfo=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=getInfo.total_likes()
        liked=False
        if(getInfo.likes.filter(id=self.request.user.id).exists()):
            liked=True
        category_menu=Category.objects.all()
        context=super(DetailsView,self).get_context_data(*args,**kwargs)
        context["category_menu"]=category_menu
        context["likes"]=total_likes
        context["liked"]=liked
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

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('postId'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('detail',args=[str(pk)]))



    