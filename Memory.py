import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
vetor = []
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '

print(memoria)
#Aqui você deve imprimir todo o conteúdo da variável memória

while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        aux = 0
        for i in range(len(memoria)):
            if memoria[i] != 'x':
                aux +=1
                vetor.append(i)
                if aux == tamanho:
                    for j in vetor:
                        memoria[j] = letra
                    break
            elif memoria[i] != ' ':
                aux = 0
                vetor = []
            else:
                print("-------------------------Não há espaço para a informação---------------------------")
                break

        print("A informação foi alocada na posição: ", str(vetor), "Vetor ->", memoria)

        #Implemente aqui a lógica da primeira escolha
        pass
    elif opcao == 2:
        aux = 0
        vetor = []
        for cat in range(len(memoria)):
            if memoria[cat] != 'x':
                aux += 1
                vetor.append(cat)
            elif memoria[cat] == 'x':
                if aux == tamanho and memoria[cat] == 'x':
                    for dog in vetor:
                        memoria[dog] = letra
                    break
                aux = 0
                vetor = []
            else:
                print("-------------------------Não há espaço para a informação---------------------------")
                break

        print("A informação foi alocada na posição: ", str(vetor), "Vetor ->", memoria)

        pass

    elif opcao == 3:
        aux = 0
        vetor = []
        vetor2 = []
        for z in range(len(memoria)):
            if memoria[z] == ' ':
                vetor.append(z)
                aux += 1
            elif memoria[z] == 'x':
                if aux > len(vetor2):
                    vetor2 = vetor
                vetor = []
                aux = 0
        for b in range(tamanho):
            memoria[vetor2[b]] = letra


        print("A informação foi alocada na posição: ", str(vetor2), "Vetor ->", memoria)

    pass

