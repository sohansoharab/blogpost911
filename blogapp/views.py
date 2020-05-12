from django.shortcuts import render
from blogapp.models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


def Home(request):
    home = {
        'title': 'Home Page',
        'message': 'Hello! Welcome to my demo learning website! In that case I am a learner.'
        }
    return render(request, 'blogapp/index.html', context=home)


def About(request):
    contact_info={
        'name': 'MD. Soharab Hossain',
        'email': 'sohansoharab@ieee.org',
        'country': 'Bangladesh',
    }
    return render(request, 'blogapp/about.html', context=contact_info)


class PostView(ListView):
    model = Post
    template_name = 'blogapp/post.html'
    context_object_name = 'all_post'


class PostDetailsView(DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'
    context_object_name = 'main_post'
