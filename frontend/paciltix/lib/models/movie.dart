class Movie {
  int idFilm;
  final String namaFilm;
  final String description;
  final DateTime tanggal;
  final int durasi;
  final String genre;
  final int batasanUmur;
  final String cast;

  Movie(
      {required this.idFilm,
      required this.namaFilm,
      required this.description,
      required this.tanggal,
      required this.durasi,
      required this.genre,
      required this.batasanUmur,
      required this.cast});

  factory Movie.fromJson(Map<String, dynamic> json) {
    return Movie(
        idFilm: json['id_film'],
        namaFilm: json['namaFilm'],
        description: json['description'],
        tanggal: json['tanggal'],
        durasi: json['durasi'],
        genre: json['genre'],
        batasanUmur: json['batasanUmur'],
        cast: json['cast']);
  }
  dynamic toJson() => {
        'id_film': idFilm,
        'namaFilm': namaFilm,
        'description': description,
        'tanggal': tanggal,
        'durasi': durasi,
        'genre': genre,
        'batasanUmur': batasanUmur,
        'cast': cast
      };
}
