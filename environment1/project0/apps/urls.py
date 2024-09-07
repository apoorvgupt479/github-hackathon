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
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('memory', views.memory, name="memory"),

    path('datahandling/', views.datahandling, name='datahandling'),
    path('fractionsdecimals/', views.fractionsdecimals, name='fractionsdecimals'),
    path('heat/', views.heat, name='heat'),
    path('integers/', views.integers, name='integers'),
    path('lineangles/', views.lineangles, name='lineangles'),
    path('nutritioninanimals/', views.nutritioninanimals, name='nutritioninanimals'),
    path('simpleequations/', views.simpleequations, name='simpleequations'),
    path('nutritioninplants/', views.nutritioninplants, name='nutritioninplants'),
    path('fibretofabric/', views.fibretofabric, name='fibretofabric'),
    path('acidsbasessalts/', views.acidsbasessalts, name='acidsbasessalts'),
]