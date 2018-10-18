from random import randint

def roll(opis):
    # Kod kostki
    # xDy + z
    # gdzie:
    # y – rodzaj kostek, których należy użyć(np.D6, D10),
    # x – liczba rzutów kośćmi;jeśli rzucamy raz, ten parametr jest pomijalny,
    # z – liczba, którą należy dodać(lub odjąć) do wyniku rzutów(opcjonalnie).
    o=opis.lower()
    if "d" not in o:
        raise Exception("No such dice")
    else:
        letterD_index=o.index("d")

    if "+" in opis:
        operation_index=opis.index("+")
        typ_kostki = int(opis[letterD_index + 1:operation_index])
        modyfikator = int(opis[operation_index + 1:])
    elif "-" in opis:
        operation_index=opis.index("-")
        typ_kostki = int(opis[letterD_index + 1:operation_index])
        modyfikator = int(opis[operation_index + 1:])
    else:
        typ_kostki = int(opis[letterD_index + 1:])
        modyfikator=0

    liczba_rzutow=opis[0:letterD_index]
    if liczba_rzutow=='':
        liczba_rzutow=1
    else:
        liczba_rzutow = int(opis[0:letterD_index])

    # printy do testów:
    # print("typ kostki={}".format(typ_kostki))
    # print("liczba_rzutow={}".format(liczba_rzutow))
    # print("modyfikator={}".format(modyfikator))
    # i=0

    suma=0
    dozwolone=[3,4,6,8,10,12,20,100]
    # dozwolone kostki D3, D4, D6, D8, D10, D12, D20, D100
    if typ_kostki not in dozwolone:
            raise Exception("No such dice")
    else:
        while liczba_rzutow> 0:
            rzut=randint(1, typ_kostki)
            suma += rzut
            # printy do testów:
            # print("sum={}, i={}, rzut={}".format(suma,i, rzut))
            # i+=1
            liczba_rzutow -= 1

        if "+" in opis:
            return suma+modyfikator
        elif "-":
            return suma-modyfikator
        else:
            return suma
        
print(roll("2D10+10"))
print(roll("D6"))
print(roll("2D3"))
print(roll("D12-1"))