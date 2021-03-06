from rest_framework import serializers
from models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'client', 'name', 'code', 'url', 'description',)