from rest_framework.serializers import ModelSerializer

from contents.models import Content


class ContentSerializer(ModelSerializer):

    class Meta:
        model = Content
        fields = ["id", "name", "content", "video_url"]
