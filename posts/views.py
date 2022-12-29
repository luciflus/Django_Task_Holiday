from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework import authentication

from .models import Tweet, Comment, Mark_tweet, Mark_comment
from .serializers import TweetSerializer, CommentSerializer, Mark_tweetSerializer, Mark_commentSerializer

from .my_generics import MyAPIView, ListMixinAPI, CreateMiximAPI, RetrieveMiximAPI, UpdateMiximAPI, DeleteMiximAPI

from .models import Tweet, Comment, Mark_tweet, Mark_comment

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_destroy(self, serializer):
        serializer.save(user_id=self.request.user.id)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_destroy(self, serializer):
        serializer.save(user_id=self.request.user.id)

class Mark_tweetViewSet(viewsets.ModelViewSet):
    queryset = Mark_tweet.objects.all()
    serializer_class = Mark_tweetSerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_destroy(self, serializer):
        serializer.save(user_id=self.request.user.id)

class Mark_commentViewSet(viewsets.ModelViewSet):
    queryset = Mark_comment.objects.all()
    serializer_class = Mark_commentSerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user.id)
    def perform_destroy(self, serializer):
        serializer.save(user_id=self.request.user.id)