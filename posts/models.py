from django.db import models

class Tweet(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.author} - {self.title}'

class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

class Mark(models.Model):
    mark_value = models.IntegerField()
    tweet = models.OneToOneField(Tweet, on_delete=models.CASCADE, null=True)

