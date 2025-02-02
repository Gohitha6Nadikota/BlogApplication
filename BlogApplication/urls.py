from django.urls import path
from .views import HomeView,DetailsView,CreatePostView,EditPostView,DeletePostView,CreateCategoryView,CategoryView,LikeView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',DetailsView.as_view(),name="detail"),
    path('create/',CreatePostView.as_view(),name="create"),
    path('createCategory/',CreateCategoryView.as_view(),name="create_category"),
    path('article/edit/<int:pk>',EditPostView.as_view(),name="edit"),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name="delete"),
    path('category/<str:catags>',CategoryView,name="category"),
    path('like/<int:pk>',LikeView,name="like_post")
]