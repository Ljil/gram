from django.views import generic
from django.db.models import Q
from . import models


class MovieListView(generic.ListView):
    def get_queryset(self):
        if self.request.GET.get('genre'):
            return models.Movie.objects.filter(
                Q(published=True),
                Q(genres__slug=self.request.GET.get('genre'))
            ).distinct()
        else:
            return models.Movie.objects.filter(published=True)
    paginate_by = 2


class MovieDetailView(generic.DetailView):
    model = models.Movie


class PersonDetailView(generic.DetailView):
    model = models.Person
