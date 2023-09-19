from rest_framework.serializers import ModelSerializer

from accounts.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "email", "username", "is_superuser", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> Account:
        if validated_data.get("is_superuser"):
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)
