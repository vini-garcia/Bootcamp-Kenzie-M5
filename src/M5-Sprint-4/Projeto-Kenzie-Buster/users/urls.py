from django.urls import path
from users.views import UsersView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('users/', UsersView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
