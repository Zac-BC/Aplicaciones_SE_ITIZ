import 'dart:js_interop';

void main() async {
  emitirNumeros()
    .listen((value){
      print('Stream value: $value');
    });
}

Stream<int> emitirNumeros() async* {
  final valoresAEMitira= [1,2,3,4,5];

  for (int i in valoresAEMitira){
    await Future.delayed(const Duration(seconds: 1));
    yield i;
  }
}