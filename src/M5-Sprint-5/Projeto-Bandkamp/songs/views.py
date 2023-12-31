from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView, PageNumberPagination):
    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs['pk'])

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs['pk'])

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer
