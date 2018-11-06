from django.db import models

# Create your models here.
class tweetModel(models.Model):
    term = models.TextField(max_length=100, null=False)
    number = models.IntegerField(null=False)

class positiveTweets(models.Model):
    tweetText = models.TextField(max_length=1000,null=False)
    userName = models.TextField(max_length=200,default="no username")
    time = models.TextField(max_length=10,default="no time")

class negativeTweets(models.Model):
    tweetText = models.TextField(max_length=1000,null=False)
    userName = models.TextField(max_length=200,default="no username")
    time = models.TextField(max_length=10,default="no time")