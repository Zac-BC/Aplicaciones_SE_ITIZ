void main (){
    final gimnasioCeleste = GimnasioAgua(popularidad: 1000.0);
    final gimnasioPlateada = GimnasioRoca(popularidad: 600.0);

    print("Popularidad: ${gimnasioCeleste.popularidad}");
    inscribirPokemon(gimnasioCeleste);
    print("Popularidad: ${gimnasioCeleste.popularidad}");

    print("Popularidad: ${gimnasioPlateada.popularidad}");
    inscribirPokemon(gimnasioPlateada);
    print("Popularidad: ${gimnasioPlateada.popularidad}");
}

double inscribirPokemon (Gimnasio gimnasio){
    if(gimnasio.popularidad<500){
        print("El gimnasio no es popular para inscribir pokemones");
        return gimnasio.popularidad;
    }else{
        return gimnasio.popularidad +=10;
    }
}

enum Tipo{fuego, roca, agua, electrico, lucha}

abstract class Gimnasio {
    double popularidad;
    final Tipo tipo;

    Gimnasio({
        required this.popularidad,
        required this.tipo
    });

    void luchar (double grado);
}

class GimnasioAgua extends Gimnasio {
    GimnasioAgua ({required double popularidad})
    :super (popularidad: popularidad, tipo: Tipo.agua);

    @override
    void luchar(double grado) {
        // TODO: implement luchar
    }}

class GimnasioRoca extends Gimnasio{
    GimnasioRoca({required popularidad})
    :super(popularidad: popularidad, tipo: Tipo.roca);

  @override
  void luchar(double grado) {
    // TODO: implement luchar
  }}