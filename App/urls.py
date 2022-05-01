from django.urls import path
from . import views

app_name = 'App'


urlpatterns = [
    path('', views.index, name='index'),
    path('python/', views.pythonquiz, name='pythonquiz'),
    path('csharp/', views.csharpquiz, name='csharpquiz'),
    path('login/', views.loginuser, name='login'),
    path('register/', views.register, name='register'),
    path("logout", views.logoutuser, name= "logout"),
    path("score/", views.score, name= "score"),
    path('practice/', views.practice, name='practice'),
    path('see_results', views.see_results, name='see_results')
]