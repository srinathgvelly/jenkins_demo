

from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

@app.route('/run/<int:n>')
def fibo(n):
    fibonacci = []
    n1, n2 = 1,1
    count = 0
    while count<=n:
        n12 = n1+n2
        fibonacci.append(n12)
        n1 = n2
        n2 = n12
        count = n12
    return json.dumps({'Key': fibonacci})

@app.route('/get/<int:n>', methods=['GET', 'POST'])

def get(n):
    comb = []
    step_sizes = [2,3,5,8,13]
    
    if n < min(step_sizes):
        return comb

    for step_size in step_sizes:
        if n == step_size:
            comb.append([step_size])
        elif n > step_size:
            child_combos = get(n - step_size)

            for child_combo in child_combos:
                comb.append([step_size] + child_combo)


    for i in range(len(comb)):
        comb[i].sort()

    res = [list(tupl) for tupl in {tuple(item) for item in comb}]

    return json.dumps({'key': res})


app.run(host='0.0.0.0', debug=True)
