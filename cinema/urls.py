from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    CinemaHallViewSet
)

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("movie-sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)
router.register("cinema-halls", CinemaHallViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
