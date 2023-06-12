username = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha:  ")

while username == senha:
    print("Erro! Nome de usuário não pode ser igual a senha")
    print("\n Tente novamente \n")
    username = input("Digite seu nome de usuário: \n")
    senha = input("Digite sua senha:  ")

print("\n Sucesso! Registro/login concluido")
