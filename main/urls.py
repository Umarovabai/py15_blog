from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import CategoryListView, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('categories', CategoryListView.as_view()),
    path('', include(router.urls))
]