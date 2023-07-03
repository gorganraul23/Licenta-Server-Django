from django.urls import path
from users.views import LoginView, LoginViewWeb, RegisterView, users_all, users_by_id

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login-web/', LoginViewWeb.as_view(), name='login_web'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', users_all, name='users_all'),
    path('<int:id>/', users_by_id, name='users_by_id'),
]
