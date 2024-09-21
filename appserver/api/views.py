from .serializers import (OptimizationCaseSerializer, OptimizationResultSerializer,
                          ObjectiveValueSerializer, DesignValueSerializer)
from .models import OptimizationCase, OptimizationResult, ObjectiveValue, DesignValue
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from .ownpermissions import ProfilePermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


# optimization
class OptimizationCaseViewSet(viewsets.ModelViewSet):
    queryset = OptimizationCase.objects.all()
    serializer_class = OptimizationCaseSerializer

    def perform_create(self, serializer):
        # OptimizationCaseを保存
        optimization_case = serializer.save()

        max_attempt_number = optimization_case.max_attempt_number

        # 仮の設計変数
        submit_desigh_vals = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

        # 既定の回数 (ここでは10回) のOptimizationResultを作成
        for i in range(max_attempt_number):

            x = submit_desigh_vals[i]
            y = x**2

            # objectを作成
            optimization_result = OptimizationResult.objects.create(
                case=optimization_case,  # case
                attempt_number=i
            )

            design_value = DesignValue.objects.create(
                result=optimization_result,
                name='x1',
                value=x,
            )

            objective_value = ObjectiveValue.objects.create(
                result=optimization_result,
                name='y1',
                value=y,
            )


class OptimizationResultViewSet(viewsets.ModelViewSet):
    queryset = OptimizationResult.objects.all()
    serializer_class = OptimizationResultSerializer


class ObjectiveValueViewSet(viewsets.ModelViewSet):
    queryset = ObjectiveValue.objects.all()
    serializer_class = ObjectiveValueSerializer


class DesignValueViewSet(viewsets.ModelViewSet):
    queryset = DesignValue.objects.all()
    serializer_class = DesignValueSerializer
