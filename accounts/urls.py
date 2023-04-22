from django.urls import path
from accounts.views import UserDetailView, UserLoginView, UserLogoutView, UserRegisterView, LogoutConfirmView

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/confirm/', LogoutConfirmView.as_view(), name='logout_confirm'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
