from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)

        # set password and create tokens for users
        user.set_password(validated_data['password'])
        user.save()
        token, _ = Token.objects.get_or_create(user=user)
        return user