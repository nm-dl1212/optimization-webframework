from django.contrib import admin
from .models import Task, OptimizationCase, OptimizationResult, ObjectiveValue, DesignValue

# Register your models here.
admin.site.register(Task)
admin.site.register(OptimizationCase)
admin.site.register(OptimizationResult)
admin.site.register(ObjectiveValue)
admin.site.register(DesignValue)
