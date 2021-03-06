#helloworld

#secgrado.py

#Algoritmo che risolve equazioni di secondo grado nella forma "aX^2+bX+c=0".

import math #Libreria "math" (matematica)
a = input("Inserisci il valore dell'incognita di secondo grado: ") #Input dell'incognita
a = int(a) #Cast al tipo "int" (intero)
b = input("Inserisci il valore dell'incognita di primo grado: ") #Input dell'incognita
b = int(b) #Cast al tipo "int" (intero)
c = input("Inserisci il valore del termine noto: ") #Input del termine noto
c = int(c) #Cast al tipo "int" (intero)
#Costrutto "if...else" (se...altrimenti) per la risoluzioni dell'equazione:
if a==0 and b==0 and c==0: #Alternativa nel caso in cui i tre valori inserit siano pari a 0:
	print("L'equazione e' indeterminata: ammette infinite soluzioni.") #Stampa della soluzione per questa alternativa
elif a==0 and b==0: #Alternativa nel caso in cui entrambe le incognite siano pari a 0:
	print("L'equazione e' impossibile: non ammette soluzioni.") #Stampa della soluzione per questa alternativa
elif a==0: #Alternativa nel caso in cui l'incognita di secondo grado sia pari a 0:
	print("L'equazione e' di primo grado:") #Stampa della tipologia di equazione
	X = -c / b #Calcolo della soluzione
	print("Soluzione:",X) #Stampa della soluzione per questa alternativa
else: #Alternativa nel caso in cui siano presenti entrambe le incognite ed il termine noto
	print("Equazione di secondo grado, completa:") #Stampa della tipologia di equazione
	delta = b * b - 4 * a * c #Calcolo del delta
	if delta < 0: #Alternativa nel caso in cui il delta sia negativo
		Rad_D = math.sqrt(-delta) #Calcolo della radice quadrata del delta
		r = -b / (2.0 * a) #Calcolo della parte reale della soluzione
		imm = abs(Rad_D / (2.0 * a)) #Calcolo della parte immaginaria della soluzione
		print("Delta < 0: L'equazione ammette due soluzioni complesse coniugate: X1 =",r,"-i",imm ,"; X2 =",r,"+i",imm) #Stampa delle soluzioni per questa alternativa
	elif delta == 0: #Alternativa nel caso in cui il delta sia pari a 0
		print("Delta = 0: L'equazione ammette due soluzioni coincidenti: X1 = X2 =",-b / (2.0 * a)) #Stampa delle soluzioni per questa alternativa
	else: #Alternativa nel caso in cui il delta sia positivo
		Rad_D = math.sqrt(delta) #Calcolo della radice quadrata del delta
		x1 = (-b - Rad_D) / (2.0 * a) #Calcolo della prima soluzione
		x2 = (-b + Rad_D) / (2.0 * a) #Calcolo della seconda soluzione
		print("Delta > 0: L'equazione ammette due soluzioni distinte: X1=",X1,"e X2=",X2) #Stampa delle soluzioni per questa alternativa
	
	
	
