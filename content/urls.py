from django.urls import path
from .views import projects_list, experience_list

urlpatterns = [
    path('', projects_list, name='projects_list'),
    path('experience_list', experience_list, name='experience_list'),
]