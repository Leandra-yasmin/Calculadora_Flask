from cmath import sqrt
from flask import Flask,jsonify,request,  render_template


app = Flask(__name__)
#app.url_map.strict_slashes = False

@app.route('/', methods=['GET', 'POST'])
def main():
        return render_template('calculadora.html')

@app.route('/calculo', methods=['POST'])
def form():
    numero1 = request.form['N1']
    numero2 = request.form['N2']
    operacao =  request.form['operacao']
    print (operacao)

    v1 = int(numero1)
    v2 = int(numero2)

    if(operacao == 'soma'):
        resultado = v1 + v2
    
    return str(resultado)


if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)