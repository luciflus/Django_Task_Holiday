from rest_framework import serializers
from .models import Tweet, Comment, Mark_tweet, Mark_comment

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class Mark_tweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark_tweet
        fields = "__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Mark_tweet.objects.all(),
                fields=['user'],
            )]

class Mark_commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark_comment
        fields = "__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Mark_comment.objects.all(),
                fields=['user'],
            )]