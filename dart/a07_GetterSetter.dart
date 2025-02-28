void main(){

    final cuadrado = Cuadrado(lado:10.0);
    cuadrado._lado = -5.0;
    print('area: ${cuadrado.area}');
    print('lado: ${cuadrado._lado}');
}

class Cuadrado{
    double _lado;

    Cuadrado ({required lado}) : _lado = lado;

    double get area {
        return _lado*_lado;
    }

    set lado (double valor) {
        if (valor < 0){
            _lado = 0;
            print('Dato suminnistrado incorrecto');
        } else{
            _lado = valor;
        }

    }
}