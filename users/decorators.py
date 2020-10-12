from django.http import HttpResponse
from django.shortcuts import redirect

''' 
if user is verified i.e logged/ registered in they shouldn't
view the login/registered page, so they should be redirected back
to the homepage
'''

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('post_list')
        return view_func(request, *args, **kwargs)
    return wrapper_func


'''
a decorator(python decorator replacing the django inbuilt decorator) is a function
that takes in another function as a parameter, and allows us to add functionality (logic)
before the original function is called. then pass the e.g login_page function into the
view_func, then the original function i.e unauthenticated_user is first called  then
run some logic and call the wrapper_func then the view_func which for e.g is login_page
is executed
'''