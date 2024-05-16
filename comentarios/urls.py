from django.urls import path
from . import views

urlpatterns = [
    path('comentarios/', views.get_comentarios),
    path('comentarios/<int:pk>/', views.get_comentario),
    path('comentarios/create/', views.create_comentario),
    path('comentarios/update/<int:pk>/', views.update_comentario),
    path('comentarios/delete/<int:pk>/', views.delete_comentario),
]