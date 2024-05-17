from datetime import timedelta

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

class Driver(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )


class DrivingLicense(models.Model):
    license_number = models.CharField(
        max_length=10,
        unique=True,
    )

    issue_date = models.DateField()

    driver = models.ForeignKey(
        to=Driver,
        on_delete=models.CASCADE,
        related_name='license',
    )

    def __str__(self):
        expiration_date = self.issue_date + timedelta(days=365)
        return f"License with number: {self.license_number} expires on {expiration_date}!"


# Task 5

class Owner(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    model = models.CharField(
        max_length=50,
    )

    year = models.PositiveIntegerField()

    owner = models.ForeignKey(
        to=Owner,
        related_name="cars",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Model: {self.model}, Year: {self.year}, Owner: {self.owner}'


class Registration(models.Model):
    registration_number = models.CharField(
        max_length=10,
        unique=True,
    )

    registration_date = models.DateField(
        blank=True,
        null=True,
    )

    car = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE,
        related_name='registration',
        null=True,
        blank=True,
    )

    def __str__(self):
        return (
            f'Registration number: {self.registration_number}, '
            f'Registration date: {self.registration_date}, '
            f'Car: {self.car}'
        )
