import re 

def menu():

    print("1. Verificar força da senha")
    print("2. Sair")
    while True:
        try:
            escolha = int(input("Sua opção:"))
            if escolha == 1:  # se a escolha for == 1, ele executará a função de verificação
                verifypssw()
                pass
            elif escolha == 2: #Termina programa
                print("'Not all super heroes wear capes'")
                break
        except ValueError or TypeError:
            print("Você deve escolher entre 1 e 2")

pssw = 0

pontos = 0

def verifypssw():
    global pssw #não sei se tem outro jeito de fazer isso
    global pontos #minha cabeça funciona assim mesmo
    pssw = input("Sua senha:")
    pssw = str(pssw)
    aux = 0
    pontos = 0
    for i in pssw:
        pontos += 4
        if re.search("[A-Z]", i): #se i for igual a uma letra maiúscula, acumula 2 pontos
            pontos += 2
            aux += 1
        if re.search("[a-z]", i): #se i for igual a uma letra minúscula, acumula 2 pontos
            pontos += 2
            aux += 1
        if re.search("[0-9]", i): #se i for igual a um dígito, acumula 4 pontos
            pontos += 4
        if re.search("[!@#$%¨&*()[/?^~´`]", i):
            pontos += 6
            aux += 1
    if len(pssw) >= 8: #se tamanho for maior que 8 bagulhos, acumula 2 pontos
        pontos += 2
    if len(pssw)/3 >= aux: #se 3/4 forem números ou letras, acumula 2 pontos
        pontos += 2

    gradekiller() #agora ficou díficil, eu fiz a parte de adição em tipo menos de 10 minutos

def gradekiller():
    global pontos
    global pssw
    simbolo = ["!@#$%¨&*()[]/?^~´`"]
    aux = []
    aux2 = 0
    if pssw.isdigit():
        for i in range(len(pssw)):
            pontos -= 1
    if pssw.isalpha():
        for j in range(len(pssw)):
            pontos -= 1
    for z in range(len(pssw)):
        if pssw[z] == pssw[z-1]: # Se o anterior for igual ao próximo, perde-se 1 ponto.
            pontos -= 1
        if pssw[z].isupper() and pssw[z-1].isupper: # Se o anterior e o próximo forem maiúsculas, perde-se 2 pontos
            pontos -= 2
            if pssw[z-2].isupper(): # Se 3 letras consecutivas forem maiúsculas, perde-se 3 pontos
                pontos -= 3
        if pssw[z].islower() and pssw[z-1].islower: # Se o anterior e o próximo forem minúsculas, perde-se 2 pontos
            pontos -= 2
            if pssw[z-2].islower(): # Se 3 letras consecutivas forem minúsculas, perde-se 3 pontos
                pontos -= 3
        if pssw[z].isdigit() and pssw[z-1].isdigit(): # Se o anterior e o próximo forem dígitos, perde-se 2 pontos
            pontos -= 2
            if pssw[z-2].isdigit(): # Se houver 3 dígitos consecutivos, perde-se 3 pontos
                pontos -= 3
        if pssw[z] and pssw[z-1] in simbolo: # Se o anterior e o próximo forem simbolos, perde-se 2 pontos
            pontos -= 2
            if pssw[z-2] in simbolo: # Se houver 3 simbolos consecutivos, perde-se 3 pontos
                pontos -= 3
    tabela()

def tabela():
    global pontos
    global pssw
    if pontos < 20:
        print("Sua senha atingiu " + str(pontos), "pontos e foi considerada Muito Fraca")
    elif 20 <= pontos < 40:
        print("Sua senha atingiu " + str(pontos), "pontos e foi considerada Fraca")
    elif 40 <= pontos < 60:
        print("Sua senha atingiu " + str(pontos), "pontos e foi considerada Boa")
    elif 60 <= pontos < 80:
        print("Sua senha atingiu " + str(pontos), "pontos e foi considerada Forte")
    elif pontos >= 80:
        print("Sua senha atingiu " + str(pontos), "pontos e foi considerada Muito Forte")


menu()
