from django.urls import path
from . import views

urlpatterns = [
    path('', views.royxat_view, name='royxat'),
    path('qoshish/', views.qoshish_view, name='qoshish'),
    path('tahrirlash/<int:pk>/', views.tahrirlash_view, name='tahrirlash'),
    path('ochirish/<int:pk>/', views.ochirish_view, name='ochirish'),
]