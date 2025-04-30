from django.urls import path
from . import views

urlpatterns = [
    path('', views.evaluation_options, name='evaluation_options'),
    path('get-random-line/', views.get_random_line, name='get_random_line'),
    path('get-file-content/<str:type>/<str:storyId>/', views.get_file_content, name='get_file_content'),
    path('get-random-nli/', views.get_random_nli, name='get_random_nli'),
    path('get-pairwise/', views.get_pairwise, name='get_pairwise'),
    path('evaluate_summary/<str:story>/<str:summary>/', views.evaluate_summary, name='evaluate_summary'),
    path('evaluate_nli/<str:premise>/<str:hypothesis>/<str:label>/', views.evaluate_nli, name='evaluate_nli'),
    path('evaluate_pairwise/<str:question>/<str:example1>/<str:example2>/<str:label>/', views.evaluate_pairwise, name='evaluate_pairwise'),
]