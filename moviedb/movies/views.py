from django.views import generic
from . import models


class MovieListView(generic.ListView):
    def get_queryset(self):
        if self.request.GET.getlist('genre'):
            print(self.request.GET.getlist('genre'))
            return models.Movie.objects.filter(
                published=True,
                genres__slug__in=self.request.GET.getlist('genre')
            ).distinct()
        else:
            return models.Movie.objects.filter(published=True)
    paginate_by = 5


class MovieDetailView(generic.DetailView):
    model = models.Movie


class PersonDetailView(generic.DetailView):
    model = models.Person
