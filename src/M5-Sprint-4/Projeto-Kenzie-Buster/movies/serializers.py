from rest_framework import serializers
from movies.models import Movie, RatingChoices, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, required=False, default=None)
    rating = serializers.ChoiceField(
        required=False, choices=RatingChoices.choices)
    synopsis = serializers.CharField(
        max_length=None, required=False, default=None)
    added_by = serializers.EmailField(read_only=True, source="user.email")

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source="movie.title")
    bought_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    bought_by = serializers.EmailField(read_only=True, source="user.email")

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
