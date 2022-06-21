from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mysite.models import Bug
from mysite.models import UserProfileInfo, Comment



# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ['username','email','password1','password2','position']

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields =['username','email','password',]

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['role',]

class RaiseBugForm(forms.ModelForm):
    class Meta():
        model = Bug
        fields = ['title', 'description',]

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ['text',]
