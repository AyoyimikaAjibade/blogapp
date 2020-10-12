from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib import messages
from .forms import CreateUserForm, ProfileForm
from django.contrib.auth.decorators import login_required


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username} you can now Login!')
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'users/register.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('post_list')

@login_required(login_url='users:login')
def profile_page(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('users:profile')
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        form = ProfileForm(instance=profile)
    context = {'form': form}
    return render(request, 'users/profile.html', context)

