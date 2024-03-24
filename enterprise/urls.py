from django.urls import path
from . import views

#URLCONf
urlpatterns = [
    path('home/', views.home),
]