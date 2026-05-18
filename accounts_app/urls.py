from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('manager-dashboard/', views.manager_dashboard, name='manager-dashboard'),
    path('attendant-dashboard/', views.attendant_dashboard, name='attendant-dashboard'),
]