#Array para receber os numeros
numeros = []

#Laço para rodar o sistema
while True:
    #Input do que o sistema irá rodar
    print("\n1 - Inserir números")
    print("1.1 - Validação para verificar se tem algum numero adicionado")
    print("2 - Ver número par")
    print("2.1 - Ver número impar")
    print("3 - Ver maior número")
    print("3.1 - Ver menor número")
    print("4 - Ver média")
    print("5 - Ver números adicionados")
    print("5.1 - Ver quant. de números adicionados")
    print("6 - Sair")
    print("7 - Excluir todos os números")
    
    #Opçao para o usuário digitar
    escolha = input("Escolha um opção: ")

    #1 - Adicionar um número
    if escolha == "1":
       numero = int(input("Digite um número: "))
       #Adiciona um numero
       numeros.append(numero)
       print("Número adicionado!")

    #1.1 - Validação para verificar se tem algum numero adicionado
    elif escolha == "1.1":
        buscarNumero = int(input("Escolha um número adicionado: "))
        quantidade = numeros.count(buscarNumero)
        print("O numero ", buscarNumero, "aparece", quantidade, "vezes")
        for buscarNumero in numeros:
          print(buscarNumero, " está na lista!") 

    elif escolha == "1.2":
        valoresUnicos = list(set(numeros)) 
        print(valoresUnicos)     
          
    #2 - Ver número par
    elif escolha == "2":
       encontrou = False
      #Laço com números
       for n in numeros:
          if n % 2 == 0:
             print(n, " é par")
             encontrou = True

   #2 - Ver número par
    elif escolha == "2.1":
       encontrou = False
      #Laço com números
       for n in numeros:
          if n % 2 == 1:
             print(n, " é impar")
             encontrou = True
          else:
              print(n, "não é impar")

    #2.3 - Ordem crescente
    elif escolha == "2.3":
       numeros.sort()  
       print("Ordem crescente: ", numeros)
 
   #2.3.1 - Ordem decrescente
    elif escolha == "2.3.1":
       numeros.sort(reverse=True)  
       print("Ordem decrescente: ",numeros)        


    #3 - Ver maior número
    elif escolha == "3":
        if numeros:
            maior = max(numeros)
            print(maior, "é o maior")
        else:
            print("Nenhum número")
   
    #3.1 - Ver menor número
    elif escolha == "3.1":
        if numeros:
            menor = min(numeros)
            print(menor, "é o menor")        

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
         else:
             print("Nenhum número foi adicionado")
   
    #5.1 - Quantidade de números adicionados
    elif escolha == "5.1":
        if numeros:
            print("Foram adicionados: ",len(numeros), "numeros")
             
    #6 - Sair
    elif escolha == "6":
       print("Encerrando programa")
       break
    
    #7 - Excluir todos os números de um lista(numeros)
    elif escolha == "7":
        if numeros:
            numeros.clear()
            print("Todos os números foram excluidos")
    
            
    else:
       print("Opção inválida")