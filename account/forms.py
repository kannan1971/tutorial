from django import forms
from django.contrib.auth.models import User  # for putting into user tables
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required='True')

    class Meta:  # meta data about the parent class
        model = User
        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        )

    def save(self, commit='True'):
        user = super(RegistrationForm,self).save(commit='False')
        user.username=self.cleaned_data['username']
        user.firstname= self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']
        user.emailname = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']


        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email'
        }
