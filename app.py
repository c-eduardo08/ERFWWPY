# i = 1

# while i < 10:   # Cuidado com os laços infinitos, ctrl + c para abortar projeto pelo terminal
#   print(f"nossa variavel ainda é {i}")
#  i = i + 1


# print("Laço de repetiçao terminado")
# print(f"Nosso valor de i final foi  {i}")


criancas = ["Ethan", "Aurora", "Liam", "Zion"]

for kd in criancas:  # Pecorrendo os itens de uma lista com for
    print(kd)


nome = "Cadu"
print("-" * 30)

for let in nome:  # Pecorrendo o index das letras de uma palavra
    print(let)


print("-" * 30)
for index in range(
    6, 20, 2
):  # Pecorrendo index em range com for, 1° elemento - inicio, 2° elemento - Final, 3° - regra de avanço , apenas 1° obrigtri
    print(index)

print("-" * 30)
print("-" * 30)
for index in range(len(criancas)):
    print(criancas[index], index)


print("-" * 30)
print("-" * 30)
print("-" * 30)

for index in range(5):
    if index == 0:
        print("Primeira linha")
    else:
        print(f"Outras linhas {index}")
