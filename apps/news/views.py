from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category,News
from .serializers import CategorySerializer,NewsSerializer
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer