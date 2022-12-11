import 'dart:convert';
import 'package:flutter/material.dart';
import '../models/movie.dart';
import 'package:http/http.dart' as http;

class MovieProvider with ChangeNotifier {
  MovieProvider() {
    this.fetchMovies();
  }

  List<Movie> _movies = [];
  List<Movie> get movies {
    return [..._movies];
  }

  fetchMovies() async {
    const url = 'http://127.0.0.1:8000/?format=json';
    try {
      final response = await http.get(Uri.parse(url));
      if (response.statusCode == 200) {
        var data = json.decode(response.body) as List;
        _movies = data.map<Movie>((json) => Movie.fromJson(json)).toList();
        notifyListeners();
      }
    } catch (e) {
      print("Something went wrong!");
    }
  }
}
