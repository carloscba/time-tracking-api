from rest_framework import serializers
from models import Userbot

class UserbotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userbot
        fields = ('id', 'name', 'platform_id',)