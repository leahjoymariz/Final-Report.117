from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="root"),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.log_out, name='logout'),
]