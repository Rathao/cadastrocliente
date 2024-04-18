from flask import Flask, request, render_template
import mysql.connector
from cadastro import Cadastro

app = Flask(__name__)
conexao = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'bd_desafio'
)
cursor = conexao.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.form
    cad = Cadastro (
        nome=data.get('nome'),
        identidade=data.get('identidade'),
        cpf=data.get('cpf'),
        rua=data.get('rua'),
        cidade=data.get('cidade'),
        estado=data.get('estado'),
        cep=data.get('cep')
    )
    comando =f'INSERT INTO users (nome, rua, cidade, estado, identidade, cpf, cep) VALUES("{cad.nome}", "{cad.rua}", "{cad.cidade}", "{cad.estado}", {cad.identidade}, {cad.cpf}, {cad.cep})'
    cursor.execute(comando)
    conexao.commit() # quando vc edita seu banco de dados    
    return render_template('/lista_cadastrados.html')

# READ
@app.route('/lista_cadastrados')
def read():
    comando = f'SELECT * FROM users'
    cursor.execute(comando)
    resultados = cursor.fetchall() # lendo o banco de dados    
    return render_template('/lista_cadastrados.html', resultados = resultados )


if __name__ == '__main__':      
    app.run()