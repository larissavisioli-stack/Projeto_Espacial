# definir variáveis

combustivel = 100
tripulantes = []

##Definir funções

def viajar():
    # aqui vamos gastar combustível
    global combustivel
    if(combustivel >=30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você está sem combustível suficiente. Abasteça!")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio!⛽")

def status_nave():
    ##mostre a quantidade de combustível e os tripulantes
    print("------------- STATUS DA NAVE -------------")
    print(f"O combustível da nave é: {combustivel}")
    print(f"Os tripulantes da nave são: {tripulantes}")
    print("------------------------------------------")

def registrarTripulante():
    ##Pergunta o  ome do tripulante e adiciona na lista
    novoTripulante = input("Qual o nome do novo tripulante?:")
    tripulantes.append(novoTripulante)
    print("Tripuante inserido com sucesso!🚀")
def removerTripulante():
     global tripulantes

     if len(tripulantes) == 0:
         print("Não há tripulantes para serem removidos")

     else:
          tripulantes.pop()
          print(f"Tripulante removido com sucesso! os tripulantes restantes são: {tripulantes}")


### Criar um menu

while True: ##esse loop roda para sempre
    print("Bem-vindo ao menu interativo da nave. Por favor selecione uma opção")
    print("\n 1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo Tripulante | 5- Sair | 6- Remover Tripulante")
    opcao = input("Escolha:")

    if (opcao == "1"):
        status_nave()

    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registrarTripulante()

    elif (opcao == "5"):
        print("Viagem encerrada!")
        break

    elif (opcao == "6"):
        removerTripulante()




#status_nave()
# registrarTripulante()
# registrarTripulante()
# registrarTripulante()
# status_nave()

# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave()
# registrarTripulante()