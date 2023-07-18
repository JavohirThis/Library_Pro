from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import BookModel,AuthorModel
from rest_framework.response import Response
from rest_framework import generics
from .serializer import BookSerializer, AuthorSerializer
# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
class AllBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

#class DetailBookView(generics.Retrive)


class DetailDelBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class UpdateBookView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class DeleteBookView(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class AllAuthorView(generics.ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class DetailAuthorView(generics.RetrieveAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class CreateAuthorView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class UpdateAuthorView(generics.UpdateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class DeleteAuthorView(generics.DestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)
