from django.urls import path
from . import views


urlpatterns = [
    path('save', views.save_experiment_response, name='save_experiment_response'),
]
