i = 0
num = 0
lista_numeros = []

# impressao linha a linha
for i in range(0, 20):
    num += 1
    print(f"{num}")

# inline
while num <= 20:
    num += 1
    lista_numeros.append(num)
    if num == 21:
        print(lista_numeros)
