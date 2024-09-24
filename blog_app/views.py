from django.shortcuts import render, redirect
from .models import Post



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog_app/add_post.html')