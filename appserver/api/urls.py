from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import TaskViewSet, ManageUserView, UserViewSet
from .views import (OptimizationCaseViewSet, OptimizationResultViewSet)

router = routers.DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("users", UserViewSet)
router.register('cases', OptimizationCaseViewSet)
router.register('results', OptimizationResultViewSet)

urlpatterns = [
    path("myself/", ManageUserView.as_view(), name="myself"),
    path("", include(router.urls)),
]
