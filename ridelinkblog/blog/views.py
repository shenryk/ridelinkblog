from django.shortcuts import render
from .models import Post 
from django.http import HttpResponse
from django.views.generic import ListView , DetailView , CreateView , UpdateView 
from .forms import PostForm
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'


class ArticleDetialView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'
    # fields = {
    #     'title', 'content'
    # }
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = { 'title','title_tag','content'}

# def home (request):
#     context ={'posts':Post.objects.all()}
#     return render (request , 'blog/home.html',context)
# def about (request):
#     return render (request , 'blog/about.html',{'title':"About Us"})

# def contact (request):
#     return render (request , 'blog/contact.html',{'title':"Conact Us"})

# def blogContent(request):

#     return render (request,'blog/blog-content.html')
