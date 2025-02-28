void main (){
  print ("Inicio del programa");
  httpGet("https://www.ardilluda.com.mx")
    .then((value){
        print(value);
    }).catchError((err) {
      print("Error: $err");
    });
  print("Fin del programa");
}

Future<String> httpGet (String url) {
  return Future.delayed(const Duration(seconds: 2),
  () {
    throw 'Error en la peticion';
    return 'Se recibio una respuesta de la peticion http';
  });
}