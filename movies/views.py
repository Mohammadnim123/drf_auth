from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Movies
from .serializer import MoviesSerializer

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (IsAuthorOrReadOnly,)

