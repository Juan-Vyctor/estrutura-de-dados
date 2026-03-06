def multiplo(n, m) :
    if n % m == 0 :
        return True;
    else :
        return False;

def cubo(aresta) :
    print(f"Volume = {aresta**3}");
    print(f"Área = {aresta**2}");
    print(f"Perímetro = {aresta*12}");

def calculaSalario(valor, horas, extras) :
    base = valor * horas;
    extra = valor * extras * 1.5;
    return base + extra;

def minMax (lista) :
    minimo = 1000000000000;
    maximo = 0;

    for numero in lista :
        if minimo > numero :
            minimo = numero;
        if maximo < numero :
            maximo = numero;

    return [minimo, maximo];