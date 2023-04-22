from django.urls import path

from api.views import AddFavoriteView, RemoveFavoriteView, PhotoListView

urlpatterns = [
    path('photos/', PhotoListView.as_view(), name='photos_api'),
    path('photo/<int:pk>/add_favorite/', AddFavoriteView.as_view(), name='api_add_favorite'),
    path('photo/<int:pk>/remove_favorite/', RemoveFavoriteView.as_view(), name='api_remove_favorite'),
]
