from flask import render_template, request, jsonify
from serve import app
from write import *

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


@app.route('/api/confirma-consulta', methods=['POST'])
def api_confirma_consulta():
    dados = request.get_json() 
    confirmar_consulta(dados) 
    return jsonify({"status": "ok"}) 


@app.route('/api/cadastra', methods=['POST'])
def api_cadastra():
    dados = request.get_json() 
    cadastra_usuario(dados) 
    return jsonify({"status": "ok"}) 