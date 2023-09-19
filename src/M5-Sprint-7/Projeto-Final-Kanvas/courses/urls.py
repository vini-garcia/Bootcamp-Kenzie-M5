from django.urls import path

from courses.views import CourseView, CourseDetailsView, StudentView, DestroyStudentView
from contents.views import ContentView, ContentDetailsView


urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<uuid:course_id>/", CourseDetailsView.as_view()),
    path("courses/<uuid:course_id>/students/", StudentView.as_view()),
    path(
        "courses/<uuid:course_id>/students/<uuid:student_id>/", DestroyStudentView.as_view()
    ),
    path("courses/<uuid:course_id>/contents/", ContentView.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:content_id>/",
         ContentDetailsView.as_view()),
]
