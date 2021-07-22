from django.shortcuts import render
from . models import Post


def home_page(request):
    posts = Post.objects.all().order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'root/home.html', context)
