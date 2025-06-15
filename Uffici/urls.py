from django.urls import path
from .views import reparti_list, reparto_edit

urlpatterns = [
    path('reparti/',         reparti_list, name='reparti_list'),
    path('reparti/<int:pk>/', reparto_edit, name='reparto_edit'),
]
