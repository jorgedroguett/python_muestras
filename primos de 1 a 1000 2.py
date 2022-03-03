# para x mayor

primos = []

rango = range(2, 10001)

for x in rango:
    contador = 0
    for i in range(2, x + 1):
        if x % i == 0:
            contador = contador + 1
    if contador <= 1:
        primos.append(x)

print(primos)
