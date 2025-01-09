from django.urls import path
from .views import HomeView,DetailsView,CreatePostView,EditPostView,DeletePostView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',DetailsView.as_view(),name="detail"),
    path('create/',CreatePostView.as_view(),name="create"),
    path('article/edit/<int:pk>',EditPostView.as_view(),name="edit"),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name="delete")
]