from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<float(signed=True):num1>/<float(signed=True):num2>')
def addition(num1, num2):
    result = num1 + num2
    return jsonify(num1=num1, num2=num2, result=result)

@app.route('/subtract/<float(signed=True):num1>/<float(signed=True):num2>')
def subtraction(num1, num2):
    result = num1 - num2
    return jsonify(num1=num1, num2=num2, result=result)

@app.route('/multiply/<float(signed=True):num1>/<float(signed=True):num2>')
def multiplication(num1, num2):
    result = num1 * num2
    return jsonify(num1=num1, num2=num2, result=result)

@app.route('/divide/<float(signed=True):num1>/<float(signed=True):num2>')
def division(num1, num2):
    if num2 == 0:
        return jsonify(error='division by zero'), 400
    result = num1 / num2
    return jsonify(num1=num1, num2=num2, result=result)

if __name__ == '__main__':
    app.run(port=3000)
