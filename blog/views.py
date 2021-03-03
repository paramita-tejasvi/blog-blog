from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def post_list(request):
    posts = Post.objects.order_by("published_date")[::-1] # most recent first
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    # where the message should be
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) # create a form object with all fields filled up
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.info(request, "Post created")
            return redirect('post_detail', pk=post.pk)
        else:
            messages.warning(request, "Error creating post")
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


@login_required
def drafts(request):
    # filter out all posts without a published date
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')[::-1]
    return render(request, 'blog/drafts.html', {'posts': posts})


@login_required
def publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    messages.info(request, "Posted!")
    return redirect('post_detail', pk=pk)


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.info(request, "Commented!")
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

