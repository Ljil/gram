from django.db import models

# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    title = models.CharField("Жанр", max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Person(models.Model):
    name = models.CharField("Имя", max_length=150)
    birth_date = models.DateField("Дата рождения")
    death_date = models.DateField("Дата смерти", blank=True, null=True)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to='star_images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "Участник съёмок"
        verbose_name_plural = "Участники съёмок"


class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    release_date = models.DateField("Дата выхода")
    tagline = models.CharField("Слоган", max_length=100, blank=True)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to='posters/')
    genres = models.ManyToManyField(
        Genre, verbose_name="Жанры", related_name="movies")
    directors = models.ManyToManyField(
        Person, verbose_name="Режиссёры", related_name="as_director")
    actors = models.ManyToManyField(
        Person, verbose_name="Актёры", related_name="as_actor")
    published = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
