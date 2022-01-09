from rest_framework import serializers
from .models import Profile
from rest_framework.authtoken.models import Token

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'token'
        ]
    def get_username(self, obj):
        return obj.user.username

    def get_token(self, obj):
        return obj.Token.token
