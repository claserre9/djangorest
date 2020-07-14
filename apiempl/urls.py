from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiempl import views
router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('post',views.UserForumPostViewSet)
router.register('comment',views.UserCommentViewSet)

urlpatterns = [
    path('login/', views.UserLoginAPIViews.as_view()),
    path('', include(router.urls))
]