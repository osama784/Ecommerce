from django.urls import path

from users import views


urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('sign-up/', views.register_user, name='register-user')

]