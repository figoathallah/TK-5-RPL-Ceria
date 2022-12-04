from django.db import models

class Movie(models.Model):
    id_film = models.AutoField(primary_key=True, editable=False)
    namaFilm = models.CharField()
    description = models.TextField()
    tanggal = models.DateField()
    durasi = models.TimeField()
    genre = models.CharField()
    batasanUmur = models.CharField()
    cast = models.TextField()
    seats = ""


    def __str__(self):
        return self.namaFilm