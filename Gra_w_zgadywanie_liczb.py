from random import randint

def guess():
    wylosowana=randint(1,100)
    while True:
        try:
            liczba =int(input("Zgadnij liczbę: "))

            if liczba>0 and liczba<101:
                if liczba<wylosowana:
                    print("Za mało!")
                elif liczba>wylosowana:
                    print("Za dużo!")
                else:
                    print("Zgadłeś!")
                    break
            else:
                print("Podaj liczbę z zakresu 1-100")
                continue
        except ValueError:
            print("To nie jest liczba")
            continue

guess()