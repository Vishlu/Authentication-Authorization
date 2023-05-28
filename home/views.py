from django.forms import widgets
from django.forms.fields import CharField
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import Edit_Profile, Register_Forms, Edit_Profile, Edit_AdminProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from home import forms


def register(request):
    if request.method == 'POST':
        form = Register_Forms(request.POST, auto_id=True)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Manager') # Data control language like giving the permission to the user with any group
            user.groups.add(group)
            messages.success(
                request, "Your account has been created successfully!.")
    else:
        form = Register_Forms(auto_id=True)
    return render(request, 'home/register.html', {'fm': form})


def login_form(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            log = AuthenticationForm(auto_id=True, request=request, data=request.POST)
            if log.is_valid():
                user = log.cleaned_data['username']
                pas = log.cleaned_data['password']
                valid = authenticate(username=user, password=pas)
                if valid is not None:
                    login(request, valid)
                    messages.success(request, 'logged in successfully!')
                    return redirect('profile')
        else:
            log = AuthenticationForm(auto_id=True)
    else:
        return redirect('profile')
    return render(request, 'home/login.html', {'login': log})


def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = Edit_AdminProfile(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = Edit_Profile(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, "profile changed.")
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = Edit_AdminProfile(instance=request.user)
                users = User.objects.all()
            else:
                fm = Edit_Profile(instance=request.user)
                users = None
        return render(request, 'home/profile.html', {'user': request.user.username, 'form': fm, 'users': users})
        
    else:
        return redirect('login')
        # note@786sagar vote@786somnath darshan123@gamer dvf gbfcg ryeh


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'password changeed')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'home/changepassword.html', {'fm': form})
    else:
        return redirect('login')


def change_password2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'password changeed')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'home/change2.html', {'fm': form})
    else:
        return redirect('login')


def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = Edit_AdminProfile(instance=pi)
        return render(request, 'home/userprofile.html', {'form': fm})
    else:
        return redirect('login')
