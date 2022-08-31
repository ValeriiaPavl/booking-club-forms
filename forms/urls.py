from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_handler),
    path('register/', views.register_handler)
]
