from django.contrib.auth.models import Group
from rest_framework import serializers
from users.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_name', 'email', 'first_name', "last_name",
                  'password', 'groups', 'is_active', 'last_login', 'start_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_active = True
        instance.save()
        if groups is not None:
            instance.groups.set(groups)

        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance.email = validated_data.get('email', instance.email)
        instance.user_name = validated_data.get(
            'user_name', instance.user_name)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        if password is not None:
            instance.set_password(password)
        groups = validated_data.pop('groups', instance.groups)
        if groups is not None:
            instance.groups.set(groups)
        instance.save()
        return instance


class ClientSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_name', 'email',
                  'password', 'is_active', 'last_login', 'start_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_active = True
        instance.is_client = True
        instance.save()

        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance.email = validated_data.get('email', instance.email)
        instance.user_name = validated_data.get(
            'user_name', instance.user_name)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        if password is not None:
            instance.set_password(password)
        groups = validated_data.pop('groups', instance.groups)
        if groups is not None:
            instance.groups.set(groups)
        instance.save()
        return instance


class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if not user.is_client:
            token = super().get_token(user)
            return token


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.is_client:
            token = super().get_token(user)
            return token
