from django.urls import path, include
from django.urls.conf import include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
]
