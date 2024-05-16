from django.urls import path
from . import views

urlpatterns = [
  path('noticias/', views.get_noticias),
  path('noticias/<int:pk>/', views.get_noticia),
  path('noticias/create/', views.create_noticia),
  path('noticias/update/<int:pk>/', views.update_noticia),
  path('noticias/delete/<int:pk>/', views.delete_noticia),
]