from rest_framework import serializers
from .models import UserNew


class UserNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNew
        fields = ('username', 'groups', 'role', 'offer', 'avatar')