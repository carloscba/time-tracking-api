from rest_framework import serializers
from models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'client_name', 'created_date',)