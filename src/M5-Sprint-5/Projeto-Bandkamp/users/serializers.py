from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                new_password = value
            setattr(instance, key, value)

        instance.save()

        user_password = User.objects.get(username=instance.username)
        user_password.set_password(new_password)
        user_password.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "full_name",
            "artistic_name",
            "password"
        ]
