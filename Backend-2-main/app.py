from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

# index principal 
@app.route('/')
def principal():
    titulo = 'En la URL define /(Operacion)/(numero1)/(numero2)'

# suma 
@app.route('/suma/<float:numero1>/<float:numero2>')
@app.route('/suma/<int:numero1>/<int:numero2>')
@app.route('/suma/<int:numero1>/<float:numero2>')
@app.route('/suma/<float:numero1>/<int:numero2>')
def suma(numero1, numero2):
    titulo = 'Suma'
    resultado = f'el resultado de {numero1} + {numero2} es: {numero1 + numero2}'
    data = {
        'resultado': resultado,
        'operacion': 'Suma'
    }
    return jsonify(data)

# Resto de las operaciones (resta, multiplicación, etc.) aquí...

if __name__ == '__main__':
    app.run(debug=True)
