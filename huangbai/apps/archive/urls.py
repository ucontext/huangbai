from django.urls import path
from . import views

urlpatterns = [
    path('aqfw', views.ArchiveView.as_view())
]