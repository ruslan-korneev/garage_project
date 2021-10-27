from django.urls import path

from . import views


urlpatterns = [
    path('register', views.PokemonCreateAPIView.as_view(), name='register-pokemon'),
]
