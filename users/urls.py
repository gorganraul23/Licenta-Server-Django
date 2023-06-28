from django.urls import path
from users.views import LoginView, LoginViewWeb, RegisterView, users_list, users_detail

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login-web/', LoginViewWeb.as_view(), name='login_web'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', users_list, name='users_list'),
    path('<int:id>/', users_detail, name='users_detail'),
]
