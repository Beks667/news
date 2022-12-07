from .models import News,Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'title',
                  'description',
                  'photo',
                  'date_of_upload',
                  'likes',
                  'news_category',)