from django.db import models

class Movie(models.Model):
    id_film = models.AutoField(primary_key=True, editable=False)
    namaFilm = models.CharField(max_length=100)
    description = models.TextField()
    tanggal = models.DateField()
    durasi = models.TimeField()
    genre = models.TextField()
    batasanUmur = models.CharField(max_length=3)
    cast = models.TextField()
    seats = ""


    def __str__(self):
        return self.namaFilm