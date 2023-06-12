nome = input("Digite seu nome(maior que 3 letras): ")
while len(nome) < 3:  # Essa mesma condiçao nao funciona com 'for', por que ?
    print("Nome negado, tente novamente do zero")
    nome = input("Digite seu nome(maior que 3 letras): ")

idade = int(input("Informe sua idade(VALÍDA): "))
while (idade < 0) & (idade > 150):
    print("Idade negada!!! Tente novamente")
    idade = int(input("Informe sua idade(VALÍDA): "))

salario = float(input("Digite seu salario: "))
while salario < 0:
    print("Salario negativo nao existe !!! Tente novamente \n")
    salario = float(input("Digite seu salario: "))

sexo = input("Digite seu sexo - f para feminino / m para masculino : ")
while (sexo != "f") and (
    sexo != "m"
):  # Uso do 'and' invés do 'or' pois nao exatamente as duas condiçoes precisam ser obedecidas E nao podem ser obedecidas numa string única
    print("Sexo nao reconhecido!!! Tente novamente")
    sexo = input("biologicamente voce deve ser m ou f: ")

civil = input("Informe seu estado civil(s/c/v/d): ")
while (civil != "s") and (civil != "c") and (civil != "v") and (civil != "d"):
    print("Estado civil nao reconhecido. Tente novamente")
    civil = input("Informe seu estado civil(s/c/v/d): ")


print("-" * 30)
print("\n Parabéns. Registro concluído com sucesso, obrigado!")
print("-" * 30)
