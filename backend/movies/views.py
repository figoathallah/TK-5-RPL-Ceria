from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie

@api_view(['GET'])

# temp for me to remember
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Returns the movies that are currently showing'
        },

        {
            'Endpoint': '/movies/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single movie object to view details on'
        },

        {
            'Endpoint': '/movies/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new movie in the database'
        },

        {
            'Endpoint': '/movies/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing movie with new data'
        },

        {
            'Endpoint': '/movies/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a movie in the database'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getMovies(request):
    movies = Movie.objects.all()
    serialized = MovieSerializer(movies, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getMovie(request, pk):
    movie = Movie.objects.get(id_film=pk)
    serialized = MovieSerializer(movie, many=False)
    return Response(serialized.data)

@api_view(['POST'])
def createMovie(request):
    data = request.data

    movie = Movie.objects.create(
        id_film = data['id_film'],
        namaFilm = data['namaFilm'],
        description = data['description'],
        tanggal = data['tanggal'],
        durasi = data['durasi'],
        genre = data['genre'],
        batasanUmur = data['batasanUmur'],
        cast = data['cast']
    )
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateMovie(request, pk):
    data = request.data
    movie = Movie.objects.get(id_film=pk)
    serializer = MovieSerializer(movie, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMovie(request, pk):
    movie = Movie.objects.get(id_film=pk)
    movie.delete()
    return Response('Movie deleted.')