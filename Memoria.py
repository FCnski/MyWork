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

while True:
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    
    if(opcao == 1):
        aux = 0
        for i in range(len(memoria)):
            if memoria[i] != 'x':
                aux +=1
                vetor.append(i)
                if aux == tamanho:
                    for j in vetor:
                        memoria[j] = letra
                        print("A informação foi alocada na posição: ", str(vetor), "Vetor ->", memoria)
                    break
            elif memoria[i] != ' ':
                aux = 0
                vetor = []
            else:
                print("-------------------------Não há espaço para a informação---------------------------")
                break
        pass
    elif opcao == 2:
        aux = 0
        vetor = []
        for i in range(len(memoria)):
            if memoria[i] != 'x':
                aux += 1
                vetor.append(i)
            elif memoria[i] == 'x':
                if aux == tamanho and memoria[i] == 'x':
                    for j in vetor:
                        memoria[j] = letra
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
        
    if(opcao == 4):
        print("Untill next time! :D")
        break
    
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utilizada")
    letra = input()

