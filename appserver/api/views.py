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

from .svc.services import SamplingService


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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # OptimizationCaseを保存
        optimization_case = serializer.save(user_id=self.request.user.id)

        # サンプリングサービスを使用して設計変数を生成
        sampling_service = SamplingService(optimization_case)
        submit_designs = sampling_service.generate_designs()

        # OptimizationResultを作成
        # 繰り返しoptimization-resultを作成
        for i in range(optimization_case.max_attempt_number):

            optimization_result = OptimizationResult.objects.create(
                case=optimization_case,  # case
                attempt_number=i
            )

            x = submit_designs[i]
            design_value = DesignValue.objects.create(
                result=optimization_result,
                name='x1',
                value=x,
            )

            y = x**2
            objective_value = ObjectiveValue.objects.create(
                result=optimization_result,
                name='y1',
                value=y,
            )


class OptimizationResultViewSet(viewsets.ModelViewSet):
    queryset = OptimizationResult.objects.all()
    serializer_class = OptimizationResultSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ObjectiveValueViewSet(viewsets.ModelViewSet):
    queryset = ObjectiveValue.objects.all()
    serializer_class = ObjectiveValueSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class DesignValueViewSet(viewsets.ModelViewSet):
    queryset = DesignValue.objects.all()
    serializer_class = DesignValueSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
