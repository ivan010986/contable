from django.urls import path
from usuario.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',LoginView,name ='LoginView'),
    # path('login', auth_views.LoginView.as_view(), name='login'),
]

