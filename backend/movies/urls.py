from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies),
    path('movies/create', views.createMovie),
    path('movies/<str:pk>/update', views.updateMovie),
    path('movies/<str:pk>/delete', views.deleteMovie),
    path('movies/<str:pk>/', views.getMovie)
]