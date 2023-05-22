from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsStaff, IsStaffOrRetrieve
from users.models import User


class TaskView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaff]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskToDoView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(status="todo")


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaffOrRetrieve]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = "task_id"

    def perform_update(self, serializer):
        if "user_id" in self.request.data:
            user_id = self.request.data["user_id"]
            user = User.objects.get(pk=user_id)
            serializer.save(user=user)
        else:
            serializer.save()
