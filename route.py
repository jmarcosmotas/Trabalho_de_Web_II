from flask import render_template, request, jsonify, Response, session
from database.queries import *
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

@app.route('/consultas-confirmadas')
def consultas_confirmados():
    return render_template('consultas_comfirmada.html')


@app.route('/api/info', methods=['GET'])
def api_info():
    especialidade_id = request.args.get("especialidade")
    hospital_id = request.args.get("hospital")
    especialidade, medico, hospital, horario_semana = informacoes_medicas(especialidade_id, hospital_id)
    if not medico or not especialidade or not hospital:
        return jsonify({"erro": "Dados não encontrados"}), 404
    informacoes = {
        "medico": medico.nome,
        "CRM": medico.crm,
        "especialidade": especialidade.especialidade,
        "endereco": hospital.endereco,
        "texto": medico.texto,
        "seg": horario_semana.segunda.split(",") if horario_semana.segunda else [],
        "ter": horario_semana.terca.split(",") if horario_semana.terca else [],
        "qua": horario_semana.quarta.split(",") if horario_semana.quarta else [],
        "qui": horario_semana.quinta.split(",") if horario_semana.quinta else [],
        "sex": horario_semana.sexta.split(",") if horario_semana.sexta else [],
        "sab": horario_semana.sabado.split(",") if horario_semana.sabado else [],
        "dom": horario_semana.domingo.split(",") if horario_semana.domingo else [],
    }   
    print(informacoes)
    return jsonify(informacoes)

    


@app.route('/api/login', methods=['POST'])
def api_login():
    dados = request.get_json()
    info_usuario = fazer_login(dados)
    if info_usuario:
        session['user'] = info_usuario
        return jsonify(info_usuario), 200
    else:
        return jsonify({"error": "CPF ou senha inválidos"}), 401

@app.route('/api/informacoes', methods=['GET'])

def api_informacoes():
    info = request.args.get("informacoes") 
      
    if info == "cidade":
        list_cid, id_cid = listar_cidades()
        return jsonify({"cidade": list_cid, "id": id_cid})
    elif info == "hospital":
        cidade_id = request.args.get("cidade_id")
        list_hos, id_hos = busca_hospital(cidade_id)
        return jsonify({"hospital": list_hos, "id": id_hos})
    elif info == "especialidade":
        hospital_id = request.args.get("hospital_id")
        list_esp, id_esp = busca_especialista(hospital_id)

        return jsonify({"especialidade": list_esp, "id": id_esp})

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
            return autenticar(cpf, senha)
        except Exception:
            return False

    @wraps(f)
    def wrapped(*args, **kwargs):
       
        if session.get('user'):
            return f(*args, **kwargs)
        if check_basic():
            return f(*args, **kwargs)
        return _unauthorized_json()

    return wrapped


@app.route('/api/confirma-consulta', methods=['POST'])
@requires_session_or_basic
def api_confirma_consulta():
    dados = request.get_json()
    confirmacao = confirmar_consulta(dados)
    if confirmacao:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"error": "A pessoa só pode ter uma consulta por vez"}), 400


@app.route('/api/cadastra', methods=['POST'])
def api_cadastra():
    dados = request.get_json()  
    
    cadastro_confirmado = cadastra_usuario(dados)

    if cadastro_confirmado:
        return jsonify({"status": "ok"}), 200 
    else:
        return jsonify({"error": "Usuário já cadastrado"}), 400


@app.route('/api/consultas-comfirmadas', methods=['POST'])
def api_consultas_confirmados():
    dados = request.get_json()
    consulta = consultas_agendadas(dados)
    if consulta:
        return jsonify({"status": "ok", **consulta}), 200
    else:
        return jsonify({"error": "Usuário não possui nenhuma Consulta Agendada"}), 400



