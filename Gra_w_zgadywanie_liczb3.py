from flask import Flask,request
from random import randint,shuffle
app=Flask(__name__)

@app.route("/")
def hello():
    form="""
        <form action="/zgadywanka3" method='GET'>
        <button type="submit">Zgaduj</button>
    """
    return "Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach."+form

@app.route("/zgadywanka3", methods=['GET', 'POST'])
def zgadywanka3():
    global guess
    min=0
    max=101

    form = """
        <form action="/zgadywanka3" method='POST'>
        {}
        <label>Liczba:
            <input type="text" name="guess" value="{}"></input>
            <input type="text" name="min" value="{}"></input>
            <input type="text" name="max" value="{}"></input>
            
        <button type="submit" name="wybor" value="wiecej">Więcej</button>
        <button type="submit" name="wybor" value="mniej">Mniej</button>
        <button type="submit" name="wybor" value="trafiles">Trafiłeś</button>
        </form>
"""
    i=0
    while i<10:
        if request.method == "GET":
            guess = int((max - min) / 2) + min
            return form.format("",guess,min,max)
        else:
            guess=int(request.form['guess'])
            if request.form["wybor"]=="trafiles":
                min=0
                max=101
                guess=int((max - min) / 2) + min
                return form.format("Wygrałeś",guess, min, max)
            elif request.form["wybor"]=="mniej":
                max=guess

                if guess == min and max - min == 1:
                    guess += 1
                elif guess == max and max - min == 1:
                    min -= 1
                    guess = int((max - min) / 2) + min
                else:
                    guess = int((max - min) / 2) + min
                i+=1
                return form.format("",guess, min, max)
            elif request.form["wybor"]=="wiecej":
                min=guess

                if guess == min and max - min == 1:
                    guess += 1
                elif guess == max and max - min == 1:
                    min -= 1
                    guess = int((max - min) / 2) + min
                else:
                    guess = int((max - min) / 2) + min
                i+=1
                return form.format("",guess,min,max)



app.run(debug=True)

# while i < 11:
#     print("Zgaduję:{}, próba:{}".format(guess, i))
#     hint = input("Zgadłem?(tak,nie): ")
#     if hint == "tak":
#         print("Wygrałem!!!")
#         break
#     elif hint == "nie":
#         hint = input("Za dużo?(tak,nie): ")
#         if hint == "tak":
#             max = guess
#             # print("guess={},max={},min={}".format(guess,max,min))
#             i += 1
#         elif hint == "nie":
#             hint = input("Za mało?(tak,nie): ")
#             if hint == "tak":
#                 min = guess
#                 # print("guess={},max={},min={}".format(guess, max, min))
#                 i += 1
#             elif hint == "nie":
#                 print("Nie oszukuj")
#                 # print("guess={},max={},min={}".format(guess, max, min))
#                 continue
#         else:
#             print("Podaj poprawną odpowiedź tak/nie:")
#     else:
#         print("Podaj poprawną odpowiedź tak/nie:")
#     if guess == min and max - min == 1:
#         guess = guess + 1
#     else:
#         guess = int((max - min) / 2) + min