from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/movies',
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