from django.contrib import admin
from django.urls import path

# import views file from app folder
from mainApp import views

# django admin header customization
# text
admin.site.site_header = "Admin Section Header"
admin.site.site_title = "Title"
admin.site.index_title = "Index Page Title"
    
urlpatterns = [
# sign-in/sign-out pages
# login
	path('login/', views.login, name='login'),
# logout
	path('logout/', views.logoutuser, name='logout'),

# homepage
    path('', views.index, name="home"),
# change [pageName] with your page name
# url address path name: [pathName]
# function name defined in views.py: [viewsFunctionName]
# page name: [pageName]
#	path('pathName', views.viewsFunctionName, name="pageName" ),
# add path address below -->
# # page:
#	path('pathName', views.viewsFunctionName, name="pageName" ),

# todo list:
# form page:
	path('todolist/form', views.todolistform, name="todolistform" ),
# data base page:
	path('todolist/table', views.todolisttable, name="todolisttable" ),

# blog:
# blog page:
	path('blog/blog', views.blog, name="blog" ),
# blogpost page:
	path('blog/blogpost<str:slug>', views.blogpost, name="blog" ),


# api --> django rest framework
	path('api/', views.drf_api, name="api" ),


]


	