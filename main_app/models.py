from django.db import models


# Task 1
class Author(models.Model):
    name = models.CharField(
        max_length=40,
    )


class Book(models.Model):
    title = models.CharField(
        max_length=40,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    # Owner
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
    )


# Task 2

class Song(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
    )


class Artist(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    songs = models.ManyToManyField(
        to=Song,
        related_name="artists",
    )


# Task 3
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    description = models.TextField(
        max_length=200,
    )

    rating = models.PositiveSmallIntegerField()

    product = models.ForeignKey(
        to=Product,
        related_name='reviews',
        on_delete=models.CASCADE,
    )

# Task 4
