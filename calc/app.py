from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_op():

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(add(a, b))

@app.route('/sub')
def sub_op():

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a, b))

@app.route('/mult')
def mult_op():

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a, b))

@app.route('/div')
def div_op():

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a, b))


op = {
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult
}

@app.route('/math/<operator>')
def operations(operator):
    operation = op[operator]
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operation(a, b))