from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from users import views


urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', obtain_auth_token, name='login')
]