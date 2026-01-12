import random

numero_segreto = random.randint(1, 100)
tentativi = 0
indovinato = False

print("Indovina il numero tra 1 e 100")

while not indovinato:
    scelta = int(input("Inserisci un numero: "))
    tentativi += 1

    if scelta < numero_segreto:
        print("Troppo basso!")
    elif scelta > numero_segreto:
        print("Troppo alto!")
    else:
        indovinato = True
        print(f"Hai indovinato in {tentativi} tentativi!")
