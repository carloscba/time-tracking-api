from models import Task
from rest_framework import viewsets
from rest_framework import permissions
from serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
