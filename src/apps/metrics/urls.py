from django.urls import path

from . import views


urlpatterns = [
    path('', views.metric_view),
]
