from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class meta:
        model = Article
        fields = ['id', 'title', 'author']