from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_wall),
    path('log_out/', views.log_out),
    path('create_message/', views.create_message),
    path('add_message/', views.add_message),
    path('create_comment/', views.create_comment),
    path('add_comment/', views.add_comment),
    path('delete_comment/', views.delete_comment),
    path('delete_message/', views.delete_message),
]