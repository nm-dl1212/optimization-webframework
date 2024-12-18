from rest_framework import serializers
from .models import Task, OptimizationCase, OptimizationResult, ObjectiveValue, DesignValue
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_date):
        user = User.objects.create_user(**validated_date)
        Token.objects.create(user=user)
        return user


class TaskSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'created_at', 'updated_at']


# optimization
class OptimizationCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptimizationCase
        fields = '__all__'
        read_only_fields = ['user_id', 'created_at']


class ObjectiveValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectiveValue
        fields = ['name', 'value']


class DesignValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignValue
        fields = ['name', 'value']


class OptimizationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptimizationResult
        fields = ['id', 'case_id', 'trial_number', 'created_at']


class DetailOptimizationResultSerializer(serializers.ModelSerializer):
    design_values = DesignValueSerializer(
        many=True, source='designvalue_set', read_only=True)
    objective_values = ObjectiveValueSerializer(
        many=True, source='objectivevalue_set', read_only=True)

    class Meta:
        model = OptimizationResult
        fields = [
            'id', 'case_id', 'trial_number', 'created_at',
            'design_values', 'objective_values'
        ]
