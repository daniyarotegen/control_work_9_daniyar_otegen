from django.urls import path
from accounts.views import UserDetailView

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
