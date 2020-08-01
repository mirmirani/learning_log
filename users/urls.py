from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    #Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    
    #  path('login/', login, {'template_name': 'users/login.html'}, name='login'),

    # Logout page
    path("logout/", views.logout_view, name='logout'),
    # no logoutView only redirect so view method needed
    
    #no template as logout will return to homepage


    # Registration
    path("register/", views.register, name='register'),


]

