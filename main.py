from flask import *
app = Flask(__name__)

convidados = ['tiberio','adson','risonelha','lauany','mariana','antonio','joao pedro']

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/trabalheaqui')
def trabalheconosco():
    return render_template('trabalheaqui.html')


@app.route('/verificar_convite', methods=['POST'])
def verificar_pessoa():
    nome_pessoa = request.form.get('nome_pessoa')
    if nome_pessoa in convidados:
        return 'vc foi convidado'
    else:
        return 'nem apareça na festa'


app.run(debug=True)