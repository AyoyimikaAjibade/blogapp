from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
#from .decorators import unpermitted_user
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts':posts}
    return render(request, 'blog/post_list.html', context)


@login_required(login_url='users:login')
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)


@login_required(login_url='users:login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)


@login_required(login_url='users:login')
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', id=post.id)
        else:
            form = PostForm(instance=post)
        context = {'form':form}
        return render(request, 'blog/post_form.html', context)
    else:
        return HttpResponse('You are not authorized to edit this post')



@login_required(login_url='users:login')
#@unpermitted_user
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')
        context = {'post': post}
        return render(request, 'blog/post_delete_form.html', context)
    else:
        return HttpResponse('You are not authorized to delete this post')


@login_required(login_url='users:login')
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True,author__username=request.user).order_by('-created_date')
    context = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', context)

@login_required(login_url='users:login')
def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        post.publish()
        context = {'post': post}
        return render(request, 'blog/post_draft_list.html', context)
    else:
        return HttpResponse('You are not authorized to publish this post')


@login_required(login_url='users:login')
def post_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'blog/post_comment_form.html', context)


@login_required(login_url='users:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('post_detail', id=comment.post.id)



@login_required(login_url='users:login')
def comment_approve(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approve()
    return redirect('post_detail', id=comment.post.id)



