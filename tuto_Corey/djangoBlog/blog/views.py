################################################################################
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
################################################################################

################################################################################
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    #Esto es lo que va a aparecer en nuestro template
    context_object_name = 'posts'
    #Para que aparescan del mas nuevo al mas viejo
    ordering = ['-date_posted']
    paginate_by = 4
################################################################################

################################################################################
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html' #<app>/<model>_<viewtype>.html
    #Esto es lo que va a aparecer en nuestro template
    context_object_name = 'posts'
    #Para que aparescan del mas nuevo al mas viejo
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
################################################################################


################################################################################
class PostDetailView(DetailView):
    model = Post
################################################################################

################################################################################
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
################################################################################

################################################################################
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
################################################################################

################################################################################
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/' #Home page
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
################################################################################


################################################################################
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
################################################################################

################################################################################
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
################################################################################