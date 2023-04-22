from django.urls import path
from gallery.views import PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, AddFavoriteView, \
    RemoveFavoriteView

urlpatterns = [
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/<int:pk>/add_favorite/', AddFavoriteView.as_view(), name='add_favorite'),
    path('photo/<int:pk>/remove_favorite/', RemoveFavoriteView.as_view(), name='remove_favorite'),
]
