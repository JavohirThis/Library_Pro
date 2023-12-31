from rest_framework import serializers
from .models import BookModel, AuthorModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('__all__')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('__all__')

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('__all__')