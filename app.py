from flask import Flask
from random import randint
app = Flask(__name__)

ANSWER = randint(0, 9)

@app.route('/<int:number>')
def number_site(number):
    if ANSWER == number:
        return 'Grats'
    else:
        return 'Try'

@app.route('/')
def start():
    return '<center>' \
           '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/VM9S5IeIK5hFm/giphy.gif">' \
           '</center>'

if __name__ == '__main__':
    app.run(debug=True)



