from django.urls import path

from contents.views import ContentView, ContentDetailsView

urlpatterns = [
    path("courses/<course_id>/contents/", ContentView.as_view()),
    path("courses/<course_id>/contents/<uuid:content_id>/",
         ContentDetailsView.as_view()),
]
