from django.views import generic
from . import models


class MovieListView(generic.ListView):
    def get_queryset(self):
        if self.request.GET.get('genre'):
            return models.Movie.objects.filter(
                published=True,
                genres__slug=self.request.GET.get('genre')
            ).distinct()
        else:
            return models.Movie.objects.filter(published=True)
    paginate_by = 2


class MovieDetailView(generic.DetailView):
    model = models.Movie


class PersonDetailView(generic.DetailView):
    model = models.Person
