from flask import Flask,request
from random import randint,shuffle
app=Flask(__name__)

@app.route("/")
def hello():
    form="""
        <form action="/zgadywanka3" method='GET'>
        <button type="submit">Zgaduj</button>
    """
    return "Pomyśl liczbę od 0 do 1000 a ja ją zgadnę."+form

@app.route("/zgadywanka3", methods=['GET', 'POST'])
def zgadywanka3():
    global guess
    global max
    global min

    form = """
        <form action="/zgadywanka3" method='POST'>
        {}
        <label>Liczba:
            <input type="text" name="answer" value="{}"></input>
        <button type="submit" name="wybor" value="wiecej">Więcej</button>
        <button type="submit" name="wybor" value="mniej">Mniej</button>
        <button type="submit" name="wybor" value="trafiles">Trafiłeś</button>
        </form>
"""
    if request.method == "GET":
        min=0
        max=1000
        guess = int((max - min) / 2) + min
        return form.format("",guess)
    else:
        guess=int(request.form['answer'])
        if request.form["wybor"]=="trafiles":
            min=0
            max=1000
            guess=int((max - min) / 2) + min
            return form.format("Wygrałeś",guess)
        elif request.form["wybor"]=="mniej":
            max=int(request.form['answer'])
            if guess == min and max - min == 1:
                guess += 1
            elif guess == max and max - min == 1:
                guess -= 1
            else:
                guess = int((max - min) / 2) + min
            return form.format("",guess)
        elif request.form["wybor"]=="wiecej":
            min=int(request.form['answer'])
            if guess == min and max - min == 1:
                guess += 1
            elif guess == max and max - min == 1:
                guess -= 1
            else:
                guess = int((max - min) / 2) + min
            return form.format("",guess)



app.run(debug=True)

