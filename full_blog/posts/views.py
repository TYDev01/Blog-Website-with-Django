from django.shortcuts import render
from .models import Posts

# Create your views here.
def posts(request):
    posts = Posts.objects.all().order_by('-time')
    return render(request, 'posts/posts_list.html', {'posts': posts})