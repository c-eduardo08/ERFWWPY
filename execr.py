# resource w/help
ano = 0
popuA = int(input("População do país A: "))
while popuA < 0:
    popuA = int(input("População do país, deve ser maior que 0: "))

taxaA = float(input("Taxa de crescimento do país A: "))

popuB = int(input("\n Poulação do país B: "))
while popuB < 0:
    popuB = int(input("População do país, deve ser maior que 0: "))

taxaB = float(input("Taxa de crescimento do país B: "))

if popuA < popuB:
    if taxaA < taxaB:
        print(
            "Isso jamais acontecerá. A população do país A, nunca irá ultrapassar a do pais B, nem em milhões de anos "
        )
    else:
        while popuA < popuB:
            ano = ano + 1
            popuA = int((1 + (taxaA / 100) * popuA))
            popuB = int((1 + (taxaB / 100) * popuB))
            print(f"ano: {ano}")
            print(f"População A : {popuA}")
            print(f"População B: {popuB}")

    if ano == 0:
        print("O país A não ultrapassa o país B, nunca.")
    print(f"O país A ultrapassa o país B, em população no ano de : {ano}")
