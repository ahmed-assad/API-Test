from django.urls import path
from . import viewsurlpatterns =[
    path('guitars', views.guitars_handler),
    path('guitars/<int:guitar_id>', views.get_guitar_with_id),
]