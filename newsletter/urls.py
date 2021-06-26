from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_list_signup, name='email_list_signup'),
]
