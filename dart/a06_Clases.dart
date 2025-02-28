void main(){
    final snorlax = Pokemon(
        nombre:"Snorlax",
        habilidad:"Ser gordito",
        dentroDePokebola:true,
        pv:100);
    
    print('Pokemon: $snorlax');
    print('nombre: ${snorlax.nombre}');
    print('habilidad: ${snorlax.habilidad}');

    final Map<String, dynamic> rawJson = {
        'nombre' : 'charizard',
        'habilidad' : 'Lanzallamas',
        'dentroDePokebola' : false,
        'pv': 500.0
    };

    final charizard = Pokemon.fromJson(rawJson);
    print(charizard);
    print('nombre: ${charizard.nombre}');
    print('habilidad: ${charizard.habilidad}');

}

class Pokemon{
    String nombre;
    String habilidad;
    bool dentroDePokebola;
    double pv;
    
    Pokemon({
        this.nombre = "",
        this.habilidad = "",
        this.dentroDePokebola = false,
        this.pv=0
    });

    Pokemon.fromJson(Map<String, dynamic> json):
        nombre = json['nombre'] ?? '',
        habilidad = json['habilidad'] ?? 'sin habilidad',
        dentroDePokebola = json['dentroDePokebola'] ?? false,
        pv = json['pv'] ?? 0;

    @override
    String toString(){
        return '$nombre - $pv';
    }
}