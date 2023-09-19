from django.urls import path
from rest_framework_simplejwt import views
from .views import LoginJWTView

urlpatterns = [
    path("token/", LoginJWTView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]
