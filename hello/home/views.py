
from django.shortcuts import render, HttpResponse
# import pyrebase
from django.shortcuts import render, redirect
from django.contrib import auth
import json
from django.http import JsonResponse

# from distutils.dep_util import newuser

# from .models import users
# from .forms import UserForm
# from django.contrib.auth.models import authenticate, login
from django.views.generic import View


# database model
# from .models import vaparkarte


# from home.forms import UserForm
# from firebase_admin import db
# from .models import User
# Create your views here.

# config={
#     "apiKey" : "AIzaSyA9t00lrtVNxa5TuQjzBSv1XppFBL73y8k",
#     "authDomain" : "kvl-doctor.firebaseapp.com",
#     "databaseURL": "https://kvl-doctor-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "projectId" : "kvl-doctor",
#     "storageBucket" : "kvl-doctor.appspot.com",
#     "messagingSenderId" : "215123281569",
#     "appId" : "1:215123281569:web:7131a595685f36fa6f52e0",
# }
# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()

# home/views.py
# from django.shortcuts import render
# from .forms import UserForm

# def user_create_view(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
           
#     else:
#         form = UserForm()
#     return render(request, 'login.html', {'form': form})


def login(request):
     return render(request, 'login.html')


def doctor(request):
     return render(request, 'doctor.html')

def index(request):
     return render(request, 'index.html')

def medicine(request):
     return render(request, 'medicine.html')

def contact(request):
     return render(request, 'contact.html')

def service(request):
     return render(request, 'service.html')
















# class UserFormView:
#      form_class=UserForm
#      template_name='Template/login'

#      def get(self, request):
#           form=self.form_class(None)
#           return render(request, self.template_name, {'form':form})
     
#      def post(self, request):
#           form=self.form_class(request.POST)

#           if form.is_valid():
#                user=form.save()
#                username=form.cleaned_data({'username'})
#                password=form.cleaned_data({'password'})
#                user.set_password(password)
#                user.save()
          

#                # newuser=authenticate(username=username, password=password)

#                if newuser is not None:
#                     if newuser.is_active:
#                          login(request, newuser)
#                          return redirect('index')
#           return render(request, self.template_name, {'form':form})


