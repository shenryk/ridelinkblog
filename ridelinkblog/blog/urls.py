from django.urls import path
# from . import views
from .views import HomeView,AddPostView, ArticleDetialView , UpdatePostView , DeletePostView , LikeView


urlpatterns = [
    path('',HomeView.as_view(),name ="home"),
    path('article/<int:pk>',ArticleDetialView.as_view(), name ='article-detail'),
    path ('add_post/',AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name ='update-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name ='delete-post'),
    path('like/<int:pk>',LikeView,name="like_post")
    # path('',views.home, name="blog-home"),
    # path('about/',views.about, name="blog-about"),
    # path('contact/',views.contact, name="blog-conatct"),
    # path('posts/',views.blogContent, name="blog-content"),
]