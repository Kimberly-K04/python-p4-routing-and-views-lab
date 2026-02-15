#!/usr/bin/env python3

from shlex import join
from flask import Flask

app = Flask(__name__)
@app.route("/")

def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/count/<parameter>")
def count(parameter):
    result = ""
    for i in range(int(parameter)):
        result += f"{i}\n"
    return result

@app.route("/print/<parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route("/math/<num1>/<path:operation>/<num2>")
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "%":
        result = num1 % num2 if num2 != 0 else "Error: Modulo by zero"
    else:
        return f"Invalid operation: {operation}"
    
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
