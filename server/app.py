#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)  # Print the string in the console
    return f'{string_param}'  # Display it in the web browser


@app.route('/count/<int:int_param>')
def count(int_param):
    numbers = '\n'.join(map(str, range(0, int_param)))
    return f'\n{numbers}'


# Math view
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # Use 'div' for division
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation"

    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
