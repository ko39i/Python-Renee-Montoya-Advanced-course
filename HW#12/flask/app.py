from flask import Flask, render_template, request, redirect

app = Flask(__name__)



@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

def calculator(val_1, val_2, action):
    try:
        val_1 = int(val_1)
    except ValueError:
        return 'value does not fit'
    try:
        val_2 = int(val_2)
    except ValueError:
        return 'value does not fit'
    if action == '+':
        result = val_1 + val_2
    elif action == '-':
        result = val_1 - val_2
    elif action == '*':
        result = val_1 * val_2
    elif action == '/':
        result = val_1 / val_2
    else:
        result = 'no value'
    return result

@app.route('/calc/<val_1>/<val_2>/<op>', methods=["GET", "POST"])
def act(val_1, val_2, op):
    action = ['+', '-', '*', '/']
    if op == 'sum':
        op = '+'
    elif op == 'dif':
        op = '-'
    elif op == 'mul':
        op = '*'
    elif op == 'div':
        op = '/'
    result = calculator(val_1, val_2, op)
    return render_template('calc.html', val_1=val_1, val_2=val_2, action=op, result=result)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=1515, debug=True)


