from django.urls import path
from . import views

app_name = 'libreria'

urlpatterns = [
    path('crear/', views.crear_libro, name='crear_libro'),
    path('', views.lista_libros, name='lista_libros'),
    path('detalle/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
