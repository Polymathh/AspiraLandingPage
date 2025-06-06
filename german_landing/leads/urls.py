from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='enroll'),
    path('success/', views.success_page, name='successs'),
    path('dashboard/', views.dashboard, name='admin'),
    path('dashboard/mark-followed/<int:lead_id>/', views.mark_followed, name='mark_followed'),
]

