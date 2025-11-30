from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    dependencies = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), many=True
    )

    class Meta:
        model = Task
        fields = "__all__"
        