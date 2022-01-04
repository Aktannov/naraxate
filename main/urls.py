from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import CategoryListView, PostsViewSet

router = DefaultRouter()
router.register('posts', PostsViewSet)

urlpatterns = [
    path('category', CategoryListView.as_view()),
    path('', include(router.urls))
]
