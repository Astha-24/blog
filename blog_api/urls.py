from django.urls import path, include

from rest_framework.routers import DefaultRouter
from blog_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('story',views.StoryFeedViewSet)

urlpatterns=[
        path('',include(router.urls)),
        path('login/',views.UserLoginApiView.as_view()),
]
