from rest_framework import serializers
from gallery.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'caption', 'created_at', 'author', 'favorite_users']