from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse

# import class from models
from .models import TodolistForm,Blog,DRFapi


# Create your views here.

# sign-in/sign-out pages
# login
# go to login page
def login(request):
    # when username-password is entered
    # if request.method == 'POST':
    #     # get the username and password
    #     username=request.POST.get('username')
    #     password=request.OST.get('password')
    #     # check the entered credentials are correct
    #     user=authenticate(username=username, password=password)
    #     # redirection for the credentials
    #     if user is not None:
    #         # correct credentials, redirect to self page
    #         return redirect("/")
    #     else:
    #         # incorrect credentials, redirect to login page
            return render(request, 'login.html')
# logout
# homepage
def logoutuser(request):
    logout(request)
    return render(request, 'index.html')


# homepage
def index(request):
    # get all blogs from database
    blogs=Blog.objects.all()
    # create a dictionary to pass the data to the html page
    blogContext={'blogs':blogs}
    return render(request, 'index.html',blogContext)
# method for pages
# pageName method
#   def method(request):
#       return render(request, ''pageName.html)
# # page
# def PageViewMethod(request):
#   return render(request, 'staticPage.html')

# todo list
# form page
# variableName = request.POST['form_field_name']
def todolistform(request):
    # add variable to form submission
    formContext={
        # 'key': 'value'
        # setting formsuccess as false
        'formSuccess': False
    }
    #  if a post is made, then the data is saved in the database    
    if request.method == 'POST':
        # get the data from the form
        # handle form
        name=request.POST['first_name']
        surname=request.POST['last_name']
        email=request.POST['user_email']
        description=request.POST['user_description']
        # print database fields in terminal
        # print(variableName)
        # save the data in the database
        # create a new object of the class Database
        # databaeObject=models.DatabaseClass(column_name=variableName)
        TodolistFormObject=TodolistForm(first_name=name, last_name=surname, user_email=email, user_description=description)
        # save the object in the database
        TodolistFormObject.save()
        # set the form success to true
        formContext={
            'formSuccess':True
        }
        # return success message in terminal
        print("data has been added in the database")
    return render(request, 'todolist/form.html',formContext)
# table page
def todolisttable(request):
    # get the data from the database
    todolist=TodolistForm.objects.all()
    # create a dictionary to pass the data to the html page
    todolistTableContext={'todolistdata':todolist}
    return render(request, 'todolist/table.html',todolistTableContext)


# blog
# blog page
def blog(request):
    # get the blog data from the database
    blogs=Blog.objects.all()
    # create a dictionary to pass the data to the html page
    blogContext={'blogs':blogs}
    return render(request, 'blog/blog.html',blogContext)
# blog post page
def blogpost(request):
    return render(request, 'blog/blogpost.html')
# blog search page
def blogsearch(request):
    return render(request, 'blog/blogsearch.html')


# api --> django rest framework
# DRFapi
def drf_api(request):
    # get the data from the database
    drf_api=DRFapi.objects.all()
    # create a list to pass the data to the html page
    drf_apiContext=list(drf_api.values())
    return JsonResponse({
        'drf_api':drf_apiContext
    })