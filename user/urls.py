from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet
from user.auth_views import CustomAuthToken, register_user, logout_user

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Include router URLs for full REST API
    path('', include(router.urls)),
    
    # Authentication endpoints
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('register/', register_user, name='api_register'),
    path('logout/', logout_user, name='api_logout'),
]