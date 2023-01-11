"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from accounts import views as acc_view
from posts import views

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)

router = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet)
router.register('comments', views.CommentViewSet)
router.register('mark_tweet', views.Mark_tweetViewSet)
router.register('mark_comment', views.Mark_commentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/accounts/', include(acc_router.urls)),

    path('api/token/', auth_views.obtain_auth_token),
    path('api/v-1.2/', include(router.urls))

]
