# Euclid extins
def euclidExtins(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, xx, yy = euclidExtins(b, a % b)
        x = yy
        y = xx - (a / b) * yy
        return d, x, y


# Teorema Chineza a Resturilor pentru refacerea valorii cautate dupa ce am gasit i solutii intermediare
def TeoremaChinezaAResturilor(listaConguentelor):
    (a, m) = listaConguentelor[0]
    for i in range(1, len(listaConguentelor)):
        (b, p) = listaConguentelor[i]
        k = ((b - a) * euclidExtins(m, p)[1]) % p
        a = (a + m * k) % (m * p)
        m = m * p
    return (a, m)


# Pohlig-Hellman pentru calcularea beta=alfa a puterea x mod p
def PohligHellman(beta, alpha, p):
    pminus1 = p - 1
    numarPrim = 2
    listaConguentelor = []
    while pminus1 != 1:
        rezultat = 0
        if (pminus1 % numarPrim == 0):
            while pminus1 % numarPrim == 0:
                pminus1 = pminus1 / numarPrim
                rezultat = rezultat + 1
            listaConguentelor.append(getX(beta, alpha, p, numarPrim, rezultat))
        numarPrim = numarPrim + 1
    (x, m) = TeoremaChinezaAResturilor(listaConguentelor)
    print "Valoarea cautata este: ", x


# functia returneaza valoarea x finala dupa refacerea celor i x.
# se va reface polinomul de grad puterea bazei pentru refacerea valorii finale
def getX(beta, alpha, p, q, r):
    qLaPuterear = q ** r
    pminus1 = p - 1
    bCurrent = beta
    xFinal = 0
    powerAlpha = pow(alpha, pminus1 / q) % p
    for i in range(0, r):
        powerBeta = pow(bCurrent, pminus1 / q ** (i + 1)) % p
        xCurrent = 0
        while (pow(powerAlpha, xCurrent) % p != powerBeta):
            xCurrent = xCurrent + 1
        xFinal = (xFinal + xCurrent * q ** i) % qLaPuterear
        bCurrent = ((bCurrent * euclidExtins(pow(alpha, xCurrent * q ** i) % p, p)[1]) % p)
    return (xFinal, qLaPuterear)

#Valoarea cautata este:  707
PohligHellman(13, 5, 2017)

