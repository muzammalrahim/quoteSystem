from rest_framework import serializers, validators
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from . import models


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=models.User.objects.all())])

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        # self.fields['username'].required = False

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        password = validated_data.get('password', None)
        if password is not None:
            validated_data['password'] = make_password(password)
        return super().create(validated_data)

    class Meta:
        model = models.User
        fields = '__all__'
