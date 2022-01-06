from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.models import Category, Post, Comment
from main.permissions import IsAuthor
from main.serializers import CategorySerializer, PostSerializer, CommentSerializer, PostListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'text']
    filterset_fields = ['category', 'tags']

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = PostListSerializer
        return serializer_class

    def get_permissions(self):
        # создовать пост может залогиненный пользователь
        if self.action == 'create':
            return [IsAuthenticated()]
        # изменять и удалять только автор
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        # просматривать могут все
        return []

class CommentViewSet(CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        # создовать пост может залогиненный пользователь
        if self.action == 'create':
            return [IsAuthenticated()]
        # изменять и удалять только автор
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]







#TODO: фильтрация, поиск
#TODO: избранное, лайки
#TODO: swagger