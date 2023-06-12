nota = int(input("Digite sua nota entre 0 a 10:"))

while nota < 0 or nota > 10:
    print("Valor invalido, tente novamente")
    nota = int(input("Digite sua nota entre 0 a 10:"))

print("parabens, voce conseguiu")

if nota < 7:
    print(f"Voce precisará fazer recuperação, sua nota foi {nota}")
else:
    print(f"Parabéns novamente, você foi aprovado, sua nota foi {nota}")
