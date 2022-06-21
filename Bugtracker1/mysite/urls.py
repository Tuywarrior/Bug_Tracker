from django.urls import path
from . import views

app_name = 'mysite'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('signup/',views.signupPage,name='sign-up'),


    path('mybugs/',views.mybugs,name='mybugs'),
    path('assignedBugs/',views.assignedBugs,name='assigned-bugs'),
    path('raisebug/',views.raiseBug,name='raisebug'),
    path('bug/<slug:pk>/edit/',views.BugUpdateView.as_view(),name='bug_edit'),
    path('bug/<slug:pk>/',views.BugDetail,name='bug_detail'),
    path('bug/<slug:pk>/remove/',views.BugDeleteView.as_view(),name='bug_remove'),
]
