"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from post import views
from migrations import views as migrations_views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('article', migrations_views.ArticleViewSet, basename='article')

post_router = DefaultRouter()
post_router.register('post', views.PostViewSet, basename='post')
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api-auth/', include('rest_framework.urls')),

    path('', include('migrations.urls')),

    path('post/', views.post_collection),
    path('post/<int:pk>/', views.post_element, name="pk"),

    path('article/', migrations_views.articelist),
    path('article/<int:pk>/', migrations_views.article_detail),

    path('articleclass/', migrations_views.ArticleAPIView.as_view()),
    path('articleclass/<int:id>/', migrations_views.ArticleDetails.as_view()),

    path('generic/article/<int:id>/', migrations_views.GenericAPIView.as_view()),

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    path('postviewset/', include(router.urls)),

]
