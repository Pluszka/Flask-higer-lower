from flask import Flask
from random import randint
app = Flask(__name__)

answer = randint(0, 9)
BAD_ANSWER = "https://media.giphy.com/media/NpL4D3Oc2bJUMAXF9P/giphy.gif"
GOOD_ANSWER = "https://media.giphy.com/media/o75ajIFH0QnQC3nCeD/giphy.gif"

@app.route('/<int:number>')
def number_site(number):
    global answer
    if answer == number:
        return '<center>' \
               f'<h2>U guess, the answer is {number}</h2>' \
               f'<img src={GOOD_ANSWER}>' \
               '</center>'
    elif answer > number:
        return '<center>' \
               '<h2>Number is higher.</h2>' \
               f'<image src={BAD_ANSWER}>' \
               '</center>'
    else:
        return '<center>' \
               '<h2>Number is lower.</h2>' \
               f'<image src={BAD_ANSWER}>' \
               '</center>'

@app.route('/')
def start():
    return '<center>' \
           '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/VM9S5IeIK5hFm/giphy.gif">' \
           '</center>'

if __name__ == '__main__':
    app.run(debug=True)



