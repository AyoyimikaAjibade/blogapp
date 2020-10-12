from django.shortcuts import redirect,get_object_or_404
from .models import Post

'''

def unpermitted_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        if request.user == post.author:
            return redirect('post_list')
        return view_func(request, *args, **kwargs)
    return wrapper_func
    
'''
