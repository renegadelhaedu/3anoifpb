from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/trabalheaqui')
def trabalheconosco():
    return render_template('trabalheaqui.html')

app.run(debug=True)