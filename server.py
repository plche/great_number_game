from crypt import methods
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'e74c306eb695508e8907b3b50b182ded7154b46ff4a0fe86d01f92cd8d98ef4f'

@app.before_first_request
def initialize():
    session['number'] = random.randint(1, 100)
    session['tlvisible'] = "d-none"
    session['thvisible'] = "d-none"
    session['ygvisible'] = "d-none"
    session['attempts'] = 0

@app.route('/', methods=["GET"])
def home():
    print(session['number'])
    return render_template("index.html", tlvisible=session['tlvisible'], thvisible=session['thvisible'], ygvisible=session['ygvisible'], number=session['number'], attempts=session['attempts'])

@app.route('/guess', methods=["POST"])
def guessNumber():
    numberEntered = int(request.form['guess'])
    print(numberEntered)
    if numberEntered < session['number']:
        session['tlvisible'] = ""
        session['thvisible'] = "d-none"
        session['ygvisible'] = "d-none"
    elif numberEntered > session['number']:
        session['thvisible'] = ""
        session['tlvisible'] = "d-none"
        session['ygvisible'] = "d-none"
    else:
        session['ygvisible'] = ""
        session['tlvisible'] = "d-none"
        session['thvisible'] = "d-none"
    session['attempts'] += 1
    return redirect('/')

@app.route('/playa', methods=["POST"])
def playAgain():
    session['number'] = random.randint(1, 100)
    session['tlvisible'] = "d-none"
    session['thvisible'] = "d-none"
    session['ygvisible'] = "d-none"
    session['attempts'] = 0
    return redirect('/')

if (__name__ == "__main__"):
    app.run(debug=True)