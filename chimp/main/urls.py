from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_archive),
    path('teacher', views.show_teacher),
]