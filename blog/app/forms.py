from  django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from  django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput , TextInput


# creer un utilisateur
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email',  'first_name' , 'last_name','password1' ,  'password2']

# connecter un utilisateur
        
class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=TextInput())
        password =  forms.CharField(widget=PasswordInput())

        
