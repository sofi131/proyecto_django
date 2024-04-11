from django.urls import path
from . import views

urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.portfolio_list, name='portfolio_list'),  # Nueva ruta para el portafolio
    path('contact/', views.contact_view, name='contact'),
]
