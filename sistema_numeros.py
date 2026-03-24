
#Array para receber os numeros
numeros = []    

def mostrar_menu():
     print("1 - Adicionar numero")
     print("2 - Verificar numero adicionado")
     print("3 - Lista de valores não repetidos")
     print("4 - Numeros pares")
     print("5 - Numeros impares")
     print("6 - Ordem crescente")
     print("7 - Ordem decrescente")
     print("8 - Maior numero")
     print("9 - Menor numero")
     print("10 - Ver média")
     print("11 - Ver números adicionados")
     print("12 - Ver quantidade de numeros adicionados")
     print("13 - Excluir valores da lista")
     print("14 - Excluir um valor da lista")
     print("15 - Sair do Menu")

#1 - Adicionar um número
def adicionar_numero(numeros):
     while True:
        try:
            numero = int(input("Digite um número: "))
            numeros.append(numero)
            print("Número adicionado!")
            break
        except ValueError:
            print("Digite apenas números!")
            
  
    #1.1 - Validação para verificar se tem algum numero adicionado
def validar_numero(numeros):
       while True:
          try:
             buscarNumero = int(input("Escolha um número adicionado: "))
             quantidade = numeros.count(buscarNumero)
             print(f"O {buscarNumero} aparece {quantidade} vezes")
             if buscarNumero in numeros:
              print(buscarNumero, " está na lista!") 
              break
             else:
                  print("Número não está na lista!")
          except ValueError:
              print("Número não encontrado")   
            

    #Faz uma lista dos valores adicionados que não estão repetidos
def lista_valores_nao_repetidos(numeros):
              if numeros:
                valoresUnicos = list(set(numeros)) 
                print(valoresUnicos) 
              else:   
                print("Valores não encontrados")        
          
    #2 - Ver número par
def numeros_pares(numeros):
     pares = []
     if not numeros:
      print("Lista vazia")   
      return
      #Laço com números
     for n in numeros:
                if n % 2 == 0:
                 pares.append(n) 
     else:
        print("Não há numeros pares")          
     print(pares)            
          

   #2 - Ver número par
def numeros_impares(numeros):
     impares = [] 
     if not numeros:
      print("Lista vazia")
      return      #Laço com números
     for n in numeros:
                if n % 2 == 1:
                 impares.append(n)
     else:
        print("Não há numeros impares")          
     print(impares)     
                
    #2.3 - Ordem crescente
def ordem_crescente(numeros):
           if numeros:
            numeros.sort()  
            print("Ordem crescente: ", numeros)
           else: 
            print("Não há numeros na lista para se criar uma Ordem")   
 
   #2.3.1 - Ordem decrescente
def ordem_decrescente(numeros):
           if numeros:
            numeros.sort(reverse=True)  
            print("Ordem decrescente: ",numeros)  
           else: 
            print("Não há numeros na lista para se criar uma Ordem")        


    #3 - Ver maior número
def maior_numero(numeros):
        
        if numeros:
            maior = max(numeros)
            print(maior, "é o maior")
        else:
            print("Nenhum número")
   
    #3.1 - Ver menor número
def menor_numero(numeros):
        if numeros:
            menor = min(numeros)
            print(menor, "é o menor")    
        else:
            print("Não possuem números menores na lista!")        

    #4 - Ver méidia
def ver_media(numeros):
       if numeros:
           media = sum(numeros) / len(numeros)
           print(media, "é a media")
       else:
           print("Nenhum número cadastrado")
    
    #5 - Ver números adicionados
def numeros_adicionados(numeros):
         if numeros:
             print("Foram adicionados os números: ", numeros)
         else:
             print("Nenhum número foi adicionado")
   
    #5.1 - Quantidade de números adicionados
def numeros_quantidade(numeros):
        if numeros:
            print("Foram adicionados: ",len(numeros), "numeros")
             
    #6 - Sair
def sair_menu(numeros):
       
       with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
             arquivo.write("\n".join(map(str, numeros)))
             print("Encerrando programa, dados adicionados a um arquivo")
            
    
    #7 - Excluir todos os números de um lista(numeros)
def excluir_numeros(numeros):
        if numeros:
            numeros.clear()
            print("Todos os números foram excluidos")
        else:
             print("Não tem números para excluir!")    

    #Excluir apenas um número desejado
def excluir_valor(numeros):
        while True:
            try:
                 deleteNumero = int(input("Escolha um numero a ser excluido: ")) 
                 if deleteNumero in numeros:
                   numeros.remove(deleteNumero)
                   print("O número ", deleteNumero, " foi excluído com sucesso!")
                   break 
                 else:
                      print("Numero não está na lista") 
            except ValueError:
                print("Numero não encontrado")          
    
       

#Laço para rodar o sistema
while True:
 
    print("\n========= MENU DE NUMEROS ==========")
    mostrar_menu()
    escolha = input("Escolha um numero da lista: ")
    if escolha == "1":
        adicionar_numero(numeros)
    elif escolha == "2":
        validar_numero(numeros)
    elif escolha == "3":
        lista_valores_nao_repetidos(numeros)
    elif escolha == "4":
        numeros_pares(numeros)
    elif escolha == "5":
        numeros_impares(numeros)    
    elif escolha == "6":
        ordem_crescente(numeros)   
    elif escolha == "7":
        ordem_decrescente(numeros) 
    elif escolha == "8":
        maior_numero(numeros)    
    elif escolha == "9":
        menor_numero(numeros) 
    elif escolha == "10":
        ver_media(numeros) 
    elif escolha == "11":
        numeros_adicionados(numeros)
    elif escolha == "12":
        numeros_quantidade(numeros)   
    elif escolha == "13":
        excluir_numeros(numeros)
    elif escolha == "14":
        excluir_valor(numeros)
    elif escolha == "15":
        sair_menu(numeros)
        break
    else:
        print("Nenhuma escolha foi selecionada corretamente!")           

    