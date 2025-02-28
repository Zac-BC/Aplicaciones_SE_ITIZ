abstract class Animal{}
abstract class Mamifero extends Animal{}
abstract class Ave extends Animal{}
abstract class Pez extends Animal{}
mixin Volador{
  void volar() => print("Estoy volando");
}
mixin Caminante{
  void caminar() => print("Estoy caminando");
}
mixin Nadador{
  void nadar() => print("Estoy nadando");
}

class Delfin extends Mamifero with Nadador{}
class Murcielago extends Mamifero with Volador, Caminante{}
class Gato extends Mamifero with Caminante, Nadador {}

class Paloma extends Ave with Volador,Caminante {}
class Pato extends Ave with Volador, Caminante,Nadador{}

class Tiburon extends Pez with Nadador{}
class PezVolador extends Pez with Nadador, Volador{}

void main (){
  final harold = Delfin();
  final batman = Murcielago();
  final flow = Gato();
  final stuard = Paloma();
  final donald = Pato();

  final tiburoncin= Tiburon();
  final eduardo = PezVolador();

  harold.nadar();

  batman.caminar();
  batman.volar();

  flow.caminar();
}