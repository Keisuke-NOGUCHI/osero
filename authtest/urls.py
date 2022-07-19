from django.urls import path
from . import views

urlpatterns = [
    #path('login/', views.LoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('priv', views.private_page, name='priv'),
    path('pub', views.public_page, name='pub'),
    #path('signup/', views.signup, name='signup'),
]