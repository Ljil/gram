from django.urls import path
from . import views


urlpatterns = [
    path('', views.MovieListView.as_view()),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail')
]
