from models import Userbot
from rest_framework import viewsets
from serializers import UserbotSerializer

class UserbotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Userbot.objects.all()
    serializer_class = UserbotSerializer
