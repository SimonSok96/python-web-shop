from django.urls import path
from . import views

# from .views import user_login
app_name = 'account'

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    
    path('register/', views.register, name='register'),
]