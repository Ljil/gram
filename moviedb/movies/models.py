from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    title = models.CharField("Жанр", max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Переход на главную + выборка жанра"""
        return reverse('movie_list') + '?genre=' + self.slug

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

    def get_positive_likes_count(self):
        return self.reviews.filter(liked=True).count()

    def get_negative_likes_count(self):
        return self.reviews.filter(liked=False).count()

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Gallery(models.Model):
    image = models.ImageField("Фото", upload_to='frames')
    to = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='gallery', blank=True, null=True)
    to_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='gallery', blank=True, null=True)

    def __str__(self):
        if self.to:
            return self.to.title
        elif self.to_person:
            return self.to_person.name
        else:
            return self.image.name

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField("Отзыв")
    liked = models.BooleanField("Нравится/Не нравится")
    to = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews", null=True)

    def __str__(self):
        return self.text[:40]

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
