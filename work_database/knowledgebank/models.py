from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MAXIMUM_QUESTION_LENGTH = 480
MAXIMUM_COMMENT_LENGTH = 480


class Country(models.Model):
    country = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.country)


class Client(models.Model):
    client = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.client)


class CountriesData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.country)


class ClientData(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.client)


class Question(models.Model):
    content = models.CharField(max_length=MAXIMUM_QUESTION_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.creation_date}] ' \
               f'Comment by {self.author}: {self.content[:80]}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=MAXIMUM_COMMENT_LENGTH)
    date_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
