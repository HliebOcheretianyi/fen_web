from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/<int:program_id>/', views.program_detail, name='program_detail'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
]