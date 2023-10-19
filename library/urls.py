from django.urls import path
from library import views
app_name = 'library'
 
urlpatterns = [
    path('clientes/<int:cliente_id>/', views.cliente_info, name='cliente_info'),
    path('clientes/', views.cliente, name='cliente'),
    path('', views.index, name='index'),
]