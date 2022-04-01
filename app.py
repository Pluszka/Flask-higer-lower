from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return '<center>' \
           '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/VM9S5IeIK5hFm/giphy.gif">' \
           '</center>'

if __name__ == '__main__':
    app.run(debug=True)



