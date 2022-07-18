from flask import Flask, render_template

app = Flask(__name__)

registro = ['08-07-2022','12:30','15:00',6.50,5,25]
@app.route('/')
def home():
    context = {
        'titulo':'Registro de Hora de trabajo',
        'registros':registro
    }
    return render_template('index.html',**context)
