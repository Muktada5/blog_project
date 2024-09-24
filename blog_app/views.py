from django.shortcuts import render, redirect
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/add_post.html')

# def update_task(request, post_id):
#     task = Task.objects.get(id=post_id)
#     if request.method == 'POST':
#         task.title = request.POST['title']
#         task.description = request.POST['description']
#         task.completed = 'completed' in request.POST
#         task.save()
#         return redirect('post_list')
#     return render(request, 'blog/update_task.html', {'post': post})


# def delete_task(request, post_id):
#     task = Task.objects.get(id=post_id)
#     task.delete()
#     return redirect('post_list')

