from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OptimizationCase(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255)
    max_attempt_number = models.IntegerField(default=10)
    initial_sampling_method = models.CharField(
        max_length=50, choices=(("latin", "latin"), ("random", "random")), default="latin"
    )
    objective_function = models.CharField(max_length=50)

    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Optimization Case'
        verbose_name_plural = 'Optimization Cases'


class OptimizationResult(models.Model):
    id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(OptimizationCase, on_delete=models.CASCADE)
    attempt_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Optimization Result'
        verbose_name_plural = 'Optimization Results'


class ObjectiveValue(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.ForeignKey(OptimizationResult, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Objective Value'
        verbose_name_plural = 'Objective Values'


class DesignValue(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.ForeignKey(OptimizationResult, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Design Value'
        verbose_name_plural = 'Design Values'
