from django.urls import path, include
from .views import articelist, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    path('article/',articelist),
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token),

]
