from django.urls import path
from . import views

urlpatterns = [
  path('noticias/', views.get_noticias),
  path('noticias/<str:pk>/', views.get_noticia),
  path('noticias/create/', views.create_noticia),
  path('noticias/update/<str:pk>/', views.update_noticia),
  path('noticias/delete/<str:pk>/', views.delete_noticia),
]