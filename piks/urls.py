from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit_snippet, name='edit'),
    path('delete/<int:id>/', views.delete_snippet, name='delete'),
]
