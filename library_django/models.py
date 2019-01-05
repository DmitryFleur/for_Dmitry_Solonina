from django.db import models
from django.utils.timezone import now


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookLocation(models.Model):
    room = models.IntegerField()
    rack = models.IntegerField()
    shelf = models.IntegerField()

    def __str__(self):
        return "Room %s, Rack %s, shelf %s" % (self.room, self.rack, self.shelf)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(BookLocation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Clients(models.Model):
    initials = models.CharField(max_length=300)
    dob = models.DateField()
    address = models.CharField(max_length=800)
    phone = models.IntegerField()

    def __str__(self):
        return self.initials


class OrderHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    take_date = models.DateField(default=now, editable=True)
    return_date = models.DateField(null=True)
    state = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Client %s took book '%s' at %s" % (self.client, self.book, self.take_date)
