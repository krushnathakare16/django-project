from django.contrib import admin
from django.urls import path
from home import views
from . import views
# from .views import user_create_view

urlpatterns = [
    path("index.html", views.index, name='index'),
      
    path("login", views.login, name='login'),
    path('', views.index, name='index'),
    path("medicine", views.medicine, name='medicine'),
    path("contact", views.contact, name='contact'),
    path("service", views.service, name='service'),
    path("doctor", views.doctor, name='doctor'),

    # home/urls.py
# from django.urls import path
# from .views import user_create_view

# urlpatterns = [
    # path('login', user_create_view, name='login'),



    # path("login", views.UserFormView, name='userform'),

]

            # ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            #     ('name', models.CharField(max_length=255)),
            #     ('email', models.CharField(max_length=255)),
            #     ('password', models.CharField(max_length=255)),