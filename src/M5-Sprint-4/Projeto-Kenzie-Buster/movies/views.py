from rest_framework.views import Request, Response, status, APIView
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieOrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import MyCustomPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class MoviesView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.get_queryset().order_by("id")
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(instance=result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save(user=request.user)
        serializer = MovieSerializer(instance=movie)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(instance=movie)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated | MyCustomPermission]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save(user=request.user, movie=movie)
        serializer = MovieOrderSerializer(instance=order)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
