from django.urls import path
from . import views

urlpatterns = [
    path('', views.evaluation_options, name='evaluation_options'),
    path('get-random-line/', views.get_random_line, name='get_random_line'),
    path('get-file-content/<str:type>/<str:storyId>/', views.get_file_content, name='get_file_content'),
]