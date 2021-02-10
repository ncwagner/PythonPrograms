from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
# def post_list(request):
#    return render(request, 'blog/post_list.html', {})


def post_list(request):
    post = Post.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/post_list.html',
                  {'post': post})
