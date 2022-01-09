from rest_framework import serializers
from rest_framework.authtoken.models import Token
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'id', #or pk
            # 'user',
            'source',
            'author',
            'title',
            'description',
            'urlToImage',
            "urlToPost",
            'content',
            'timestamp'
        ]
        read_only_fields = ['id', 'user']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = Post.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Opps, title has been used already")
        return value

