from django.urls import path
from . import views


urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('profile/<int:pk>', views.PersonDetailView.as_view(), name='person_detail'),
]
