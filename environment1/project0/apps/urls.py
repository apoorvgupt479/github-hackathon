from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns =[
    path('', views.hero, name='hero'),
    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('tictactoe/', views.tictactoe, name='tictactoe')
]