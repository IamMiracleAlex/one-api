from django.db import models


class Character(models.Model):
    _id = models.CharField(max_length=200)
    height = models.CharField(max_length=50, default='')
    race = models.CharField(max_length=20, default='')
    gender = models.CharField(max_length=10, default='')
    birth = models.CharField(max_length=50, default='')
    spouse = models.CharField(max_length=100, default='')
    death = models.CharField(max_length=20, default='')
    realm = models.CharField(max_length=50, default='')
    hair = models.CharField(max_length=20, default='')
    name = models.CharField(max_length=20, default='')
    wikiUrl = models.URLField(null=True)

    def __str__(self):
        return self._id
    


class Quote(models.Model):
    _id = models.CharField(max_length=200)
    dialog = models.CharField(max_length=250, default='')
    movie = models.CharField(max_length=200)
    character = models.CharField(max_length=100)


class Favourite(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    characters = models.ManyToManyField('app.Character')
    quotes = models.ManyToManyField('app.Quote')


