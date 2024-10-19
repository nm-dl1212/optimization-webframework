from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import TaskViewSet, ManageUserView, UserViewSet
from .views import (OptimizationCaseViewSet, OptimizationResultViewSet,
                    ObjectiveValueViewSet, DesignValueViewSet)

router = routers.DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("users", UserViewSet)
router.register('optim', OptimizationCaseViewSet)

urlpatterns = [
    path("myself/", ManageUserView.as_view(), name="myself"),
    path("", include(router.urls)),
]
