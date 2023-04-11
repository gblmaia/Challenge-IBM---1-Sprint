print()
print("Bom dia. Primeiro realizaremos o seu cadastro.")
print()

nome = input("Digite o seu nome completo:\n")
print()
rua = input("Perfeito. Agora digite a rua onde a irregularidade foi localizada (com numeracao):\n")
print()
exit = 0

while exit == 0:

    print("Perfeito. Vamos seguir com uma serie de perguntas relacionadas ao ocorrido agora.")

    q1 = input("Qual era o tipo do problema que foi observado? Marque: "
               "\n1 - Buraco    2 - Vazamento    3 - Lixo    4 - Outro\n")
    print()

    if q1 == "1":
        b1 = input(f"Escreva aqui uma descricao da irregularidade de buracos que voce observou"\
                   f" na rua {rua}.\n")
        print()
        print(f"Perfeito {nome}. Foi cadastrado a irregularidade da rua {rua} em nosso sistema."\
              f"\nMuito obrigado pela cooperacao.")
        exit = + 1

    elif q1 == "2":
        v1 = input(f"Escreva aqui uma descricao da irregularidade de vazamento que voce observou"\
                   f" na rua {rua}.\n")
        print()
        print(f"Perfeito {nome}. Foi cadastrado a irregularidade da rua {rua} em nosso sistema."\
              f"\nMuito obrigado pela cooperacao.")
        exit = + 1

    elif q1 == "3":
        l1 = input(f"Escreva aqui uma descricao da irregularidade de lixo que voce observou"\
                   f" na rua {rua}.\n")
        print()
        print(f"Perfeito {nome}. Foi cadastrado a irregularidade da rua {rua} em nosso sistema."\
              f"\nMuito obrigado pela cooperacao.")
        exit = + 1

    elif q1 == "4":
        o1 = input(f"Como foi escolhido a opcao ''Outro'', descreva precisamente a irregularidade"\
                   f" que foi observada na rua {rua}.\n")
        print()
        print(f"Perfeito {nome}. Foi cadastrado a irregularidade da rua {rua} em nosso sistema."\
              f"\nMuito obrigado pela cooperacao.")
        exit =+ 1

    else:
        print("INPUT INVALIDO. Apenas numeros de 1 a 4.")
        print()
