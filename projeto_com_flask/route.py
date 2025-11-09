from flask import render_template, request, jsonify, Response, session
from serve import app
from write import *
import base64
from functools import wraps

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/marca-consulta')
def marcar_consulta():
    return render_template('marcar_consulta.html')

@app.route('/confirmacao')
def confirmacao():
    return render_template('confirmacao.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/valida-email')
def valida_email():
    return render_template('valida_email.html')

@app.route('/altera-senha')
def altera_senha():
    return render_template('altera_senha.html')

@app.route('/altera-cadastro')
def altera_cadastro():
    return render_template('altera_cadastro.html')


@app.route('/api/info', methods=['GET'])
def api_info():
    info = {
        "medico":"Dr. Fulano de Tal",
        "CRM": "99999",
        "endereco":"Rua Projetada Nº 000",
        "texto":"Sou Dr. Fulano de Tal, clínico geral formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde.",
        "seg":["08:00", "09:00", "10:00", "11:00"],
        "ter":["08:00", "09:00", "10:00"],
        "qua":["08:00", "09:00", "11:00", "15:00"],
        "qui":[],
        "sex":["08:00", "14:00"],
        "sab":[],
        "dom":["08:00", "09:00", "10:00"]
    }
    return jsonify(info)


@app.route('/api/login', methods=['POST'])
def api_login():
    dados = request.get_json()
    info_usuario = fazer_login(dados)
    if info_usuario:
        # cria sessão do usuário
        session['user'] = info_usuario
        return jsonify(info_usuario), 200
    else:
        return jsonify({"error": "CPF ou senha inválidos"}), 401


@app.route('/api/informacoes', methods=['GET'])
def api_informacoes():
    info = request.args.get("informacoes")   
    if info == "cidade":
        return jsonify({"cidade": ["Picos", "Oeiras", "Teresina"]})
    elif info == "hospital":
        return jsonify({"hospital": ["Hospital Regional", "Hosp. Reg. Justino Luz", "UPA 24h"]})
    elif info == "especialidade":
        return jsonify({"especialista": ["Clínico Geral", "Cardiologia", "Dermatologia"]})


def _unauthorized_json():
    return jsonify({"error": "Unauthorized"}), 401


def requires_session_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user'):
            return _unauthorized_json()
        return f(*args, **kwargs)
    return decorated


def requires_session_or_basic(f):
    """Aceita autenticação por sessão (cookie) OU por HTTP Basic.

    - Se o cliente já tiver `session['user']`, passa.
    - Caso contrário, tenta ler o header Authorization Basic e validar via `autenticar`.
    """
    def check_basic():
        auth = request.headers.get('Authorization')
        if not auth:
            return False
        try:
            parts = auth.split(None, 1)
            if len(parts) != 2:
                return False
            scheme, creds = parts
            if scheme.lower() != 'basic':
                return False
            decoded = base64.b64decode(creds).decode('utf-8')
            cpf, senha = decoded.split(':', 1)
            # usa a função que criamos em write.py
            return autenticar(cpf, senha)
        except Exception:
            return False

    @wraps(f)
    def wrapped(*args, **kwargs):
        # primeiro tenta sessão
        if session.get('user'):
            return f(*args, **kwargs)
        # depois tenta Basic
        if check_basic():
            return f(*args, **kwargs)
        return _unauthorized_json()

    return wrapped


@app.route('/api/confirma-consulta', methods=['POST'])
@requires_session_or_basic
def api_confirma_consulta():
    dados = request.get_json()
    confirmar_consulta(dados)
    return jsonify({"status": "ok"}) 


@app.route('/api/cadastra', methods=['POST'])
def api_cadastra():
    dados = request.get_json() 
    cadastra_usuario(dados) 
    return jsonify({"status": "ok"}) 