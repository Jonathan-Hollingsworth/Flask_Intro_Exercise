from flask import Flask, request
app = Flask(__name__)

from operations import add, sub, mult, div

@app.route('/math/<operation>')
def calculate(operation):
    operations = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations[operation](a,b)
    return f'{result}'