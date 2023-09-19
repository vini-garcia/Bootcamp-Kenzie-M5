from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from courses.models import Course
from courses.serializers import CourseSerializer, CourseStudentSerializer
from courses.permissions import IsSuperuserOrMathodGet, IsSuperuser
from accounts.models import Account
from students_courses.models import StudentCourse


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrMathodGet]

    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()

        return Course.objects.filter(students=self.request.user)


class CourseDetailsView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrMathodGet]

    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

    http_method_names = ["get", "patch", "delete"]


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()

        return Course.objects.filter(students=self.request.user)


class StudentView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"

    http_method_names = ["get", "put"]


class DestroyStudentView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"

    def perform_destroy(self, serializer):
        try:
            student = get_object_or_404(Account,
                                        pk=self.kwargs["student_id"])
            student_course = StudentCourse.objects.get(
                student=student,
                course_id=self.kwargs["course_id"],
            )
            student_course.delete()
        except StudentCourse.DoesNotExist:
            error = "this id is not associated with this course."
            raise NotFound(error)
