import 'package:flutter/material.dart';
import 'package:paciltix/api/api.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MovieProvider(),
      child: MaterialApp(
        title: 'PacilTix',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: HomePage(),
      ),
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final movieProv = Provider.of<MovieProvider>(context);
    return Scaffold(
        appBar: AppBar(
          title: Text('PacilTix Dashboard'),
        ),
        body: ListView.builder(
            itemCount: movieProv.movies.length,
            itemBuilder: (BuildContext context, int index) {
              return ListTile(
                title: Text(movieProv.movies[index].namaFilm),
                subtitle: Text(movieProv.movies[index].cast),
              );
            }));
  }
}
