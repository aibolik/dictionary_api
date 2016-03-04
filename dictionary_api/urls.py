"""dictionary_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
# from django.contrib.auth.models import User
from rest_framework import routers
from dictionary_api.api.views import WordsViewSet
from dictionary_api.api.views import *
#
# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'words/en', WordsEnglishViewSet)
router.register(r'words/ru', WordsRussianViewSet)
router.register(r'words/kz', WordsKazakhViewSet)
# router.register(r'words/en/', WordsByLanguageViewSet)
# router.register(r'words', WordsByLanguageViewSet)
# router.register(r'words/(?P<language>.+)/$', WordsByLanguageViewSet)
# router.register(r'^api/words/(?P<language>\w+)/$', WordsByLanguageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

#
# class CustomRouter(routers.SimpleRouter):
#     """
#     A router for read-only APIs, which doesn't use trailing slashes.
#     """
#     routes = [
#         Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}$',
#            mapping={'get': 'retrieve'},
#            name='{basename}-detail',
#            initkwargs={'suffix': 'Detail'}
#         ),
#         DynamicDetailRoute(
#             url=r'^{prefix}/{lookup}/{methodnamehyphen}$',
#             name='{basename}-{methodnamehyphen}',
#             initkwargs={}
#         )
#     ]
