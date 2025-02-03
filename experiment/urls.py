from django.urls import path
from . import views

urlpatterns = [
    path('save', views.save_experiment_response, name='save_experiment_response'),
    path('save-time', views.save_experiment_start_time, name='save_experiment_start_time'),
]
