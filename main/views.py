from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.models import Category, Post, Comment
from main.permissions import IsAuthor
from main.serializers import CategorySerializer, PostSerializer, CommentSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class =PostSerializer

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = PostSerializer
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





#TODO: список категорий
#TODO: CRUD постов
#TODO: изображение в постах
#TODO: комменты
#TODO: подключить twilio
#TODO: авторизация
#TODO: избранное, лайки
