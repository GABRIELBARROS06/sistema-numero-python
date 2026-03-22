#Array para receber os numeros
numeros = []

#Laço para rodar o sistema
while True:
    #Input do que o sistema irá rodar
    print("\n1 - Inserir números")
    print("2 - Ver número par")
    print("3 - Ver maior número")
    print("4 - Ver média")
    print("5 - Ver números adicionados")
    print("6 - Sair")
    
    #Opçao para o usuário digitar
    escolha = input("Escolha um opção: ")

    #1 - Adicionar um número
    if escolha == "1":
       numero = int(input("Digite um número: "))
       #Adiciona um numero
       numeros.append(numero)
       print("Número adicionado!")

    
    #2 - Ver número par
    elif escolha == "2":
       encontrou = False
      #Laço com números
       for n in numeros:
          if n % 2 == 0:
             print(n, " é par")
             encontrou = True

    #3 - Ver maior número
    elif escolha == "3":
        if numeros:
            maior = max(numeros)
            print(maior, "é o maior")
        else:
            print("Nenhum número")

    #4 - Ver méidia
    elif escolha == "4":
       if numeros:
           media = sum(numeros) / len(numeros)
           print(media, "é a media")
       else:
           print("Nenhum número cadastrado")
    
    #5 - Ver números adicionados
    elif escolha == "5":
         if numeros:
             print("Foram adicionados os números: ", numeros)
             

    #6 - Sair
    elif escolha == "6":
       print("Encerrando programa")
       break
            
    else:
       print("Opção inválida")