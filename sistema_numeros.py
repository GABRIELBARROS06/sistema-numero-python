numeros = []

while True:
    print("\n1 - Inserir números")
    print("2 - Ver número par")
    print("3 - Ver maior número")
    print("4 - Ver méidia")
    print("5 - Sair")

    escolha = input("Escolha um opção: ")

    if escolha == "1":
       numero = int(input("Digite um número: "))
       numeros.append(numero)
       print("Número adicionado!")

    elif escolha == "2":
       encontrou = False
       for n in numeros:
          if n % 2 == 0:
             print(n, " é par")
             encontrou = True

    if not encontrou:
          print("Nenhum número par encontrado")

    elif escolha == "3":
        if numeros:
            maior = max(numeros)
            print(maior, "é o maior")
        else:
            print("Nenhum número")

    elif escolha == "4":
       if numeros:
           media = sum(numeros) / len(numeros)
           print(media, "é a media")
       else:
           print("Nenhum número cadastrado")

    elif escolha == "5":
       print("Encerrando programa")
       break
            
    else:
       print("Opção inválida")