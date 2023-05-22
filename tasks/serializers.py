from rest_framework import serializers
from .models import Task
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", required=False, allow_null=True
    )

    def update(self, instance: Task, validated_data: dict) -> Task:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "user_id"]
        read_only_fields = ["id"]


class TaskFormatResSerializer(serializers.ModelSerializer):
    def update(self, instance: Task, validated_data: dict) -> Task:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status"]
        read_only_fields = ["id"]
