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
class AllCreateBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

#class DetailBookView(generics.Retrive)


class DetailDelUpBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class AllCreateAuthorView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class DetailAuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)
