from django.urls import path
from . import views

urlpatterns = [
    path('', views.ambulance_services_list, name='ambulance_services'),
    path('book/<int:ambulance_id>/', views.book_ambulance, name='book_ambulance'),
]
