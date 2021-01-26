import re 

def menu():

    print("1. Verify the strenght of your password.")
    print("2. Exit.")
    while True:
        try:
            escolha = int(input("Sua opção:"))
            if escolha == 1:  # se a escolha for == 1, ele executará a função de verificação / If you choose 1, the program will execute
                verifypssw()
                pass
            elif escolha == 2: #Termina programa/End program
                print("Untill next time!")
                break
        except ValueError or TypeError:
            print("Você deve escolher entre 1 e 2")

pssw = 0

pontos = 0

def verifypssw():
    global pssw  #as variáveis precisam ser declaradas globalmente para serem utilizadas além do escopo local das funções!
    global pontos  #the variables must be declared as global as to make them usable outside of the function local scope
    pssw = input("Sua senha:")
    pssw = str(pssw)
    aux = 0
    pontos = 0
    for i in pssw: #É necessário utilizar o if pois precisamos sequenciar todas as condições e não apenas uma, então, o elif e o else tornam-se não utlizáveis
        pontos += 4 #It is necessary to use only if as our condition, because we need to go through them all once, like sequential search
        if re.search("[A-Z]", i): #se i for igual a uma letra maiúscula, acumula 2 pontos / if i equals a uppercase key, accumulates two points
            pontos += 2
            aux += 1
        if re.search("[a-z]", i): #se i for igual a uma letra minúscula, acumula 2 pontos / If i equals a lowercase key, you get two points
            pontos += 2
            aux += 1
        if re.search("[0-9]", i): #se i for igual a um dígito, acumula 4 pontos / if i equals a digit, accumulate 4 points
            pontos += 4
        if re.search("[!@#$%¨&*()[/?^~´`]", i):
            pontos += 6
            aux += 1
    if len(pssw) >= 8: #se tamanho for maior que 8, acumula 2 pontos / If there are more than 8 digits/characters in your pssw, you'll be awarded 2 points
        pontos += 2
    if len(pssw)/3 >= aux: #se 3/4 forem números ou letras, acumula 2 pontos / If 3/4 of the content of your pssw are numbers or letters, you get two points 
        pontos += 2

    gradekiller() #Função para deduzir pontos da senha/ This function will deduce points awarded by your password

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
                pontos -= 1
        if pssw[z].islower() and pssw[z-1].islower: # Se o anterior e o próximo forem minúsculas, perde-se 2 pontos
            pontos -= 2
            if pssw[z-2].islower(): # Se 3 letras consecutivas forem minúsculas, perde-se 3 pontos
                pontos -= 1
        if pssw[z].isdigit() and pssw[z-1].isdigit(): # Se o anterior e o próximo forem dígitos, perde-se 2 pontos
            pontos -= 2
            if pssw[z-2].isdigit(): # Se houver 3 dígitos consecutivos, perde-se 3 pontos
                pontos -= 1
        if pssw[z] and pssw[z-1] in simbolo: # Se o anterior e o próximo forem simbolos, perde-se 2 pontos
            pontos -= 2
            if pssw[z-2] in simbolo: # Se houver 3 simbolos consecutivos, perde-se 3 pontos
                pontos -= 1
    tabela()

def tabela():
    global pontos
    if pontos < 20:
        print("Sua senha atingiu " + str(pontos), "points and was considered Very Weak")
    elif 20 <= pontos < 40:
        print("Sua senha atingiu " + str(pontos), "points and was considered Weak")
    elif 40 <= pontos < 60:
        print("Sua senha atingiu " + str(pontos), "points and was considered Reasonable/Medium")
    elif 60 <= pontos < 80:
        print("Sua senha atingiu " + str(pontos), "points and was considered Good")
    elif pontos >= 80:
        print("Sua senha atingiu " + str(pontos), "points and was considered Great")


menu()
