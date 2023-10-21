from django.urls import path
from .views import UserLogin, UserSignup, UserLogout

app_name = 'authentication'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('registration/', UserSignup.as_view(), name='registration'),
    path('logout/', UserLogout.as_view(), name='logout'),
]