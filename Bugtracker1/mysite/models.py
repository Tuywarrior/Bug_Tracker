from turtle import title
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class UserProfileInfo(models.Model):
    ROLE = (
        ('OL', 'Organisation-Lead'),
        ('SDE1', 'SeniorDeveloper'),
        ('SDE2', 'JuniorDeveloper'),
        ('U', 'User'),
    )
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    # additional
    role = models.CharField(max_length=4, choices=ROLE, default='U')
    def __str__(self):
        return self.user.username 

class Bug(models.Model):
    SEVERITY_LEVEL = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
        ('NS', 'Not Yet Set'),
    )
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    severity_level = models.CharField(max_length=4, choices=SEVERITY_LEVEL,default='NS')
    resolved = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='assignedperson',null=True)
    deadline = models.DateTimeField(default=datetime.now())
    raised_by = models.CharField(max_length=150,blank=True,null=True)
    visibility = models.IntegerField(default=1)
    resolved_on = models.DateTimeField(default=datetime.now(), blank=True)
    opened_on = models.DateTimeField(default=timezone.now)
    assigned_on = models.DateTimeField(default=datetime.now(), blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("mysite:bug_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    bug = models.ForeignKey(Bug,related_name='bug',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("mysite:bug_detail")
    

    def __str__(self):
        return self.text

