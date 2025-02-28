void main (){

    final Map<String,dynamic> pokemon ={
        'nombre': 'Ditto',
        'habitad':'transformacion',
        'color': 'rosa',
        'hp': 80,
        'evolucion':null,
        'regio':'foso de paldea',
        'imagenes': <int,String>{
            1: "pokemon1.png",
            2: "pojemon2.png"

        }
    };

    print(pokemon);
    print(pokemon['nombre']);
    print(pokemon['imagenes'][1]);
    Map <int,String> frutos = pokemon['imagenes'];

    print(frutos[1]);
    List <String>frutas=['Manzanas','Guayabas'];
    print(frutas[1]);

    print('imagenes: $frutos');
    print('imagenes: ${pokemon['imagenes']}');
}