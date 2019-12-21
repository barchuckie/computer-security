from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('accounts/register/', views.Register.as_view(), name='register'),
  path('confirm_transfer', views.confirm_transfer, name='confirm_transfer'),
  path('new_transfer', views.new_transfer, name='new_transfer'),
  path('sql_injection', views.sql_injection, name='sql_injection'),
  path('admin/confirm', views.admin_confirm_transfers, name='admin_confirm'),
  path('admin/all_transfers', views.admin_transfers, name='admin_transfers')
]
