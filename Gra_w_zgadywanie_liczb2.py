def guess2():
    i=1
    min = 0
    max = 100
    enter=input("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach. Naciśnij enter")
    guess = int((max - min) / 2) + min
    while i<11:
        print("Zgaduję:{}, próba:{}".format(guess,i))
        hint=input("Zgadłem?(tak,nie): ")
        if hint=="tak":
            print("Wygrałem!!!")
            break
        elif hint=="nie":
            hint=input("Za dużo?(tak,nie): ")
            if hint=="tak":
                max=guess
                i+=1
            elif hint=="nie":
                hint = input("Za mało?(tak,nie): ")
                if hint=="tak":
                    min=guess
                    i+=1
                elif hint=="nie":
                    print("Nie oszukuj")
                    continue
            else:
                print("Podaj poprawną odpowiedź tak/nie:")
        else:
            print("Podaj poprawną odpowiedź tak/nie:")
        guess = int((max - min) / 2) + min

guess2()