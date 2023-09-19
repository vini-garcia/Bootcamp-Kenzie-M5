from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.views import AccountView

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
