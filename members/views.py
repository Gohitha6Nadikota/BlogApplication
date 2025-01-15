from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from .forms import SignUpForm
class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='Registration/register.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=UserChangeForm
    template_name='Registration/editinfo.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user
