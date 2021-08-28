from django.db import models


class User(models.Model):
    name = models.CharField(max_length=250)
    followers = models.ManyToManyField("graphql_api.User")
