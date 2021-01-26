 id = { 1 : "Vaca Holandesa" , 2 : "Porco", 3 : "Cabra",
 4 : "Bode", 5 : "Vaca Sindi", 6 : "Ovelha",
 7 : "Galinha", 8 : "Frango", 9 : "Boi",
 10 : "Cachorro"}
 
lista_animais = [1,2,3,4,5,6,7,8,9,10]

y = int(len(lista_animais))//2 - 1
x = input("Qual o id do animal que você quer achar?")

def AchaBixo(x, y):
 for i in range(int(len(lista_animais)) - 1):
 if x == lista_animais[y]:
 print("O animal deste ID é um(a):", id.get(x))
 break
 elif x > lista_animais[y]:
 y += 1
 elif x < lista_animais[y]:
 y -= 1
AchaBixo(int(x), int(y))
