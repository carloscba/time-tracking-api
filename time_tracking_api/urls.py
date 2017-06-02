from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User

from apps.client.views import ClientViewSet
from apps.userbot.views import UserbotViewSet
from apps.task.views import TaskViewSet
from apps.project.views import ProjectViewSet

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'usersbot', UserbotViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'projects', ProjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
]