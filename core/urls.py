from django.urls import path
from django.shortcuts import render
from .views import login_view

urlpatterns = [
    path('login/', login_view),
    path('success/', lambda request: render(request, 'success.html')),
]