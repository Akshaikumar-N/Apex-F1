from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('rate/<int:driver_id>/', views.rate_driver, name='rate_driver'),
    path('predict/<int:track_id>/', views.predict_winner, name='predict_winner'),
    path('quiz/', views.quiz, name='quiz'),
]
