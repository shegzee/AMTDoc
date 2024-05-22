from rest_framework import serializers
from .models import User, Agent, Patient, Doctor, Lga

class LgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lga
        fields = ('name',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('user', 'lga', 'town', 'phone')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('gender', 'dob', 'phone', 'address')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('user', 'name')