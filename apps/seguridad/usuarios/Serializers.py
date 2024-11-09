from .models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email']

    # Validar que las contraseñas coincidan
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Las contraseñas no coinciden'})
        return attrs

    # Crear el usuario
    def create(self, validated_data):
        validated_data.pop('password2')  # Eliminar password2 ya que no se necesita para la creación del usuario
        user = User.objects.create_user(**validated_data)  # Crear usuario con la contraseña encriptada
        return user
