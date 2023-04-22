from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import PhotoSerializer
from gallery.models import Photo


class PhotoListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Photo.objects.all()
        serializer = PhotoSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        photo = Photo.objects.get(pk=pk)
        if not photo.favorite_users.filter(pk=request.user.pk).exists():
            photo.favorite_users.add(request.user)
            photo.save()
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Photo already in favorites"}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        photo = Photo.objects.get(pk=pk)
        if photo.favorite_users.filter(pk=request.user.pk).exists():
            photo.favorite_users.remove(request.user)
            photo.save()
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Photo not found in favorites"}, status=status.HTTP_400_BAD_REQUEST)
