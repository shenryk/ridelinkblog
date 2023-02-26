from django.shortcuts import render , get_object_or_404,redirect
from .models import Post 
from django.http import HttpResponseRedirect
from django.views.generic import ListView , DetailView , CreateView , UpdateView ,DeleteView
from .forms import PostForm , EditForm, ContactForm
from django.urls import reverse_lazy, reverse
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
    success_url = reverse_lazy('home')
    
    # fields = '__all__'
    # fields = {
    #     'title', 'content'
    # }
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = EditForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

def LikeView(request , pk):
    post = get_object_or_404(Post , id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

    # fields = { 'title','title_tag','content'}

# def home (request):
#     context ={'posts':Post.objects.all()}
#     return render (request , 'blog/home.html',context)
def about (request):
    return render (request , 'blog/about.html',{'title':"About Us"})

def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Do something with the data (e.g. send an email)
            return redirect('home')
    else:
        form = ContactForm()
    return render (request , 'blog/contact.html',{'title':"Conact Us",'form':form})

# def blogContent(request):

#     return render (request,'blog/blog-content.html')
