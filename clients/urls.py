from django.urls import path

from . import views


app_name = 'clients'

urlpatterns = [
    path('', views.clients_index, name='clients_index'),
    path('<int:id>/', views.clients_details, name='clients_details'),
    path('<int:id>/edit/', views.clients_edit, name='clients_edit'),
    path('<int:id>/delete/', views.clients_delete, name='clients_delete'),
]