from django.views import generic
from . import models


# для склейки запроса
from functools import reduce
from operator import and_
from django.db.models import Q


class MovieListView(generic.ListView):
    @staticmethod
    def get_genres():
        return models.Genre.objects.all()

    def get_queryset(self):
        query = models.Movie.objects.filter(published=True)
        if self.request.GET.getlist('genre'):
            # Выбираются фильмы в которых есть хотя бы 1 жанр из списка
            # return query.filter(genres__slug__in=self.request.GET.getlist('genre')).distinct()
            # Выбираются только фильмы, удовлетворяющие всем жанрам
            return query.exclude(~reduce(and_, [Q(genres__slug=c) for c in self.request.GET.getlist('genre')])).distinct()
        return query

    paginate_by = 5


class MovieDetailView(generic.DetailView):
    model = models.Movie


class PersonDetailView(generic.DetailView):
    model = models.Person
