from django.contrib.auth.models import User, Group
#from photo.models import Photo
from rest_framework import serializers
##0419_test_django + angular


#from models import book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
"""
class Test(serializers.ModelSerializer):
    class Meta:
        model= Photo
        fields = ('description','created_at')
"""
