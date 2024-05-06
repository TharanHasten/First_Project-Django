from django.urls import path
from . import views

urlpatterns = [
    path("", views.htmlPage, name='hii'),
    path('data/', views.pageRes, name='hello'),
]