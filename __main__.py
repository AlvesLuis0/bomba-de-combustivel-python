#Participantes da equipe:
# Luis Eduardo Alves de Sousa - 202203004409
from BombaCombustivel import BombaCombustivel

tipoCombustivel = input("Tipo de Combustível: ")
valorLitro = float(input("Valor do Combustível: "))
quantidadeCombustivel = float(input("Quantidade de Combustível na Bomba [em litros]: "))

bomba = BombaCombustivel(tipoCombustivel, valorLitro, quantidadeCombustivel)

while 1:
    print("O que deseja fazer?")
    print("[1] Abastecer por valor")
    print("[2] Abastecer por litro")
    print("[3] Alterar valor do litro")
    print("[4] Alterar tipo de combustível")
    print("[5] Alterar quantidade de combustível na bomba")
    print("[6] Sair")
    i = input("- ")

    if i == "1":
        bomba.abastecerPorValor(float(input("Valor: ")))   

    elif i == "2":
        bomba.abastecerPorLitro(float(input("Quantidade [em litros]: ")))

    elif i == "3":
        bomba.alterarValor(float(input("Novo valor do litro: ")))

    elif i == "4":
        bomba.alterarCombustivel(input("Novo tipo de combustível: "))

    elif i == "5":
        bomba.alterarQuantidadeCombustivel(float(input("Quantidade a ser adicionada na bomba [em litros]: ")))

    elif i == "6":
        exit()
    
    print("\n")