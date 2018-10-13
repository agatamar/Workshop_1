from random import randint

# zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
#
#     czy wprowadzony ciąg znaków jest poprawną liczbą,
#     czy użytkownik nie wpisał tej liczby już poprzednio,
#     czy liczba należy do zakresu 1-49,


def lotto():
    i=1
    podane_liczby=[]
    wylosowane_liczby=[]
    while i<7:
        while True:
            try:
                liczba =int(input("Podaj liczbę nr {}: ".format(i)))

                if liczba>0 and liczba<50:
                    if liczba not in podane_liczby:
                        podane_liczby.append(liczba)
                        break
                    else:
                        print("Tę liczbę już podano. Podaj inną")
                        continue
                else:
                    print("Podaj liczbę z zakresu 1-49")
                    continue
            except ValueError:
                print("To nie jest liczba")
                continue
        i+=1
    podane_liczby.sort()

    for i in range(1,7):
        wylosowana=randint(1,49)
        wylosowane_liczby.append(wylosowana)
    wylosowane_liczby.sort()

    trafiona=0

    for l in podane_liczby:
        if l in wylosowane_liczby:
            trafiona+=1

    print(podane_liczby)
    print(wylosowane_liczby)
    if trafiona>=3:
        print("Wylosowano co najmniej 3!!!!")
    else:
        print("Nie wylosowano nawet marnej 3ki !!!!!")




lotto()