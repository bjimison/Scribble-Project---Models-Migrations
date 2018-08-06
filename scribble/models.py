from django.db import models

# Create your models here.

class Post(models.Model):
  author = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=100)


# ******************************* COMMENT ******************************

class Comment(models.Model):
  author = models.CharField(max_length=100)
  body = models.CharField(max_length=100)
  Post = models.ForeignKey()
