from rest_framework.serializers import ModelSerializer
from .models import Movie

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        field = '__all__'