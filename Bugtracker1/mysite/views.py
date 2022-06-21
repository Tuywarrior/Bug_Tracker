from datetime import date, timezone, datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from mysite.forms import RaiseBugForm
from mysite.forms import UserProfileInfoForm, UserForm, CommentForm
from mysite.models import UserProfileInfo, Bug, Comment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(request):
    if(not request.user.is_authenticated):
        bugs = Bug.objects.filter(resolved=True, visibility=1).order_by('-resolved_on')
        
    else:
        user = UserProfileInfo.objects.get(user=request.user)
        if(user.role == 'U' or user.role == 'SDE2'):
            bugs = Bug.objects.filter(resolved=True, visibility=1).order_by('-resolved_on')
        else:
            bugs = Bug.objects.filter(resolved=True).order_by('-resolved_on')
    
    return render(request, 'mysite/index.html',{
            'bugs' : bugs,
    })

@login_required(login_url='/login')
def assignedBugs(request):
    if(not request.user.is_authenticated ):
        return HttpResponse("You are not allowed to view this page!")
    else:
        user = UserProfileInfo.objects.get(user=request.user)
        if(user.role == 'U'):
            user = UserProfileInfo.objects.get(user=request.user)
        else:
            bugs = Bug.objects.filter(assigned_to=user.user).order_by('-assigned_on')
    
    return render(request, 'mysite/assigned_bugs.html',{
            'bugs' : bugs,
    })


@login_required(login_url='/login')
def mybugs(request):
    user = request.user
    bugs = Bug.objects.filter(raised_by=user).order_by('-opened_on')
    return render(request, 'mysite/mybugs.html',{
            'bugs' : bugs,
    })

def loginPage(request):
    if (request.method =='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mysite:index')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'mysite/login.html')
    return render(request,'mysite/login.html')   

# @login_required
def logoutUser(request):
    logout(request)
    return redirect('mysite:index')

def signupPage(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() :

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            # profile.user = user

            # profile.save()
            return redirect('mysite:login')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()
 
    return render(request,'mysite/signup.html',{'user_form':user_form,})

@login_required(login_url='login/')
def raiseBug(request):
    form = RaiseBugForm()

    if request.method == "POST":
        username = request.user.username
        print(username)
        form = RaiseBugForm(
            data=request.POST,
        )
        form= form.save()
        user = User.objects.filter(username=username)
        form.raised_by=username
        form.save()
        return redirect('mysite:bug_detail', pk=form.pk)
    return render(request, 'mysite/bug_form.html',{
        'form':form,
    })

class BugUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'mysite/bug_form.html'
    form_class = RaiseBugForm
    model = Bug

def BugDetail(request,pk):
    bug = Bug.objects.get(pk=pk)
    comment_form = CommentForm()
    if request.method == "POST":
        username = request.user.username
        print(username)
        form = CommentForm(
            data=request.POST,
        )
        form= form.save()
        user = User.objects.filter(username=username)
        form.author=username
        form.save()
        return redirect('mysite:bug_detail', pk=pk)
    return render(request, 'mysite/bug_detail.html',{
        'comment_form':comment_form,
        'object':bug,
    })



class BugDeleteView(LoginRequiredMixin,DeleteView):
    model = Bug
    success_url = reverse_lazy('mysite:mybugs') 