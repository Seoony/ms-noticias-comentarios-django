from django.urls import path
from . import views

urlpatterns = [
    path('comentarios/', views.get_comentarios),
    path('comentarios/<str:pk>/', views.get_comentario),
    path('comentarios/create/', views.create_comentario),
    path('comentarios/update/<str:pk>/', views.update_comentario),
    path('comentarios/delete/<str:pk>/', views.delete_comentario),
]