from rest_framework import serializers

from apps.users.models import UserAccountModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountModel
        fields = ['user_id', 'email', 'last_name_kanji', 'first_name_kanji']
