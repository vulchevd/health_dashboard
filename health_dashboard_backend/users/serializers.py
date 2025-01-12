from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор за модела CustomUser.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_verified']
