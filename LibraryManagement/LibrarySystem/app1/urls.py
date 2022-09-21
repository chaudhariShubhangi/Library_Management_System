from django.contrib import admin
from django.urls import path, include

from .views import retreive_books

urlpatterns = [
    path("retreive_books",retreive_books.as_view())

]