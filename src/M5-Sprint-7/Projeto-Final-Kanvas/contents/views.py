from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from courses.models import Course
from courses.permissions import IsSuperuser
from contents.serializers import ContentSerializer
from contents.models import Content
from contents.permissions import IsParticipantOrSuperuser


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs["course_id"])
        serializer.save(course=course)


class ContentDetailsView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsParticipantOrSuperuser]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    http_method_names = ["get", "patch", "delete"]


    def perform_update(self, serializer):
        get_object_or_404(Content, pk=self.kwargs["content_id"])
        return serializer.save(pk=self.kwargs["content_id"])
