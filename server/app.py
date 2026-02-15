#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:word>")
def print_string(string):
    return string

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return f"Invalid operation: {operation}"
    return f"{num1} {operation} {num2} = {result}"



if __name__ == '__main__':
    app.run(port=5555, debug=True)
