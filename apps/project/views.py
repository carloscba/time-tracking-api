from models import Project
from rest_framework import viewsets
from rest_framework import permissions
from serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
