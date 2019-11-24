from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('accounts/register/', views.Register.as_view(), name='register'),
  path('confirm_transfer', views.confirm_transfer, name='confirm_transfer'),
  path('new_transfer', views.new_transfer, name='new_transfer'),
]
