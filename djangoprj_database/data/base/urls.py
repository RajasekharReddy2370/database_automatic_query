from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.query_books, name='query_books'),
    path('htm/', views.htm, name='htm'),
]