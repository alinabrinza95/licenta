#aflarea celui mai mare divizor comun
def gcd(a, b):
    while (b != 0):
        remainder = a % b
        a = b
        b = remainder
    return a
#aflarea celuilalt element din factorizarea unui numar format din inmultirea a doua numere prime
#prin impartirea numarului initial la primul factor prin gasit in numar
def factorizare(numar, factorPrim1):
    factorPrim2=numar/factorPrim1
    print("Factorizarea numarului", numar, " este: ", factorPrim1, " si ", factorPrim2)
#algoritmul lui Pollard
#numar = numarul ca carui factorizare se doreste a afla
#bound = o limita pana la care sa se faca verificarea de fatorizare
#factorExpansiune = se extinde bound-ul in cazul in care counterul a ajuns deja la limita superioara a bound-ului
#                   si nu s-a gasit inca un factor prim in factorizarea numarului ales
def Pollard(numar, bound, factorExpansiune):
    expansiune=False
    counter=1
    var=2

    while(counter<bound):
        varNew=pow(var, counter)%numar
        d=gcd(varNew-1, numar)
        if(1<d & d<numar):
            factorizare(numar, d)
            return d
        if(counter==bound-1 and not expansiune):
            expansiune=True
            bound=bound*factorExpansiune
        var=varNew
        counter+=1
#apel de functie pentru gasirea factorizarii numarului 6715963697
Pollard(4294434817, 500, 2)
#output-ul returnat este: ('Factorizarea numarului', 4294434817L, ' este: ', 8191L, ' si ', 524287L)
#m ales doua numere mersenne in formarea numarului de testat: 8191 si 524287