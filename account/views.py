from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from account.forms import RegistrationForm,EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
# Http Response Method

# def home(request):
#     return HttpResponse('Home Page')

# Render Method ( template)

#@login_required decorator to restric login
def home(request):
    number = [1,2,3,4]
    name ='Rajesh'

    args={'myName':name, 'myList':number}
    return render(request,'account/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        x=form.is_valid()
        print(x)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:home-return'))
    else:
        form = RegistrationForm()

        arg = {'form':form }
        return render(request,'account/register.html', arg)

#@login_required
def view_profile(request):
    arg = {'user' : request.user}
    return render(request, 'account/viewprofile.html', arg)

#@login_required
def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)

        arg ={'form' : form}
        return render(request,'account/editprofile.html',arg)

#@login_required
def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data =request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect(reverse('account:view_profile'))
        else:
            return redirect(reverse('account:change-password'))
    else:
        form = PasswordChangeForm(user=request.user)

        arg ={'form' : form}
        return render(request,'account/change-password.html',arg)
