#  Esse arquivo e criado as consultas do Banco de Dados
from .models import db, Cidade, Hospital, Especialidade, Medico, HorarioSemana, Usuario, Consulta
from .init import db

def listar_cidades():
    cidades = db.session.query(Cidade).all()
    lista_cidade = [c.cidade for c in cidades]
    lista_id = [c.id for c in cidades]
    return lista_cidade, lista_id

def busca_hospital(cidade_id):
    hospitais = db.session.query(Hospital).filter_by(cidade_fk=cidade_id).all()
    lista_hospital = [h.hospital for h in hospitais]
    lista_id = [h.id for h in hospitais]
    return lista_hospital, lista_id

def busca_especialista(hospital_id):
    especialistas = db.session.query(Especialidade).filter_by(hospital_fk=hospital_id).all()    
    lista_especialista = [e.especialidade for e in especialistas]
    lista_id = [e.id for e in especialistas]
    return lista_especialista, lista_id

def informacoes_medicas(especialista_id, hospital_id):
    especialista = Especialidade.query.get(especialista_id)
    medico = Medico.query.filter_by(especialidade_fk = especialista_id).first()
    hospital = Hospital.query.get(hospital_id)
    horario_da_semana = HorarioSemana.query.filter_by(medico_fk=medico.crm).first()
    return especialista, medico, hospital, horario_da_semana

def cadastra_usuario(dados):
    usuario_existente = Usuario.query.filter_by(cpf=dados["cpf"]).first()

    if usuario_existente:
        return False 

    novo_usuario = Usuario(
        cpf=dados.get("cpf"),
        nome=dados.get("nome"),
        email=dados.get("email"),
        telefone=dados.get("telefone"),
        data_n=dados.get("dataNascimento"), 
        endereco=dados.get("endereco"),
        senha=dados.get("senha")
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return True  

def usuario_existe(cpf):
    usuario_existe = Usuario.query.filter_by(cpf=cpf).first()
    return usuario_existe

def confirmar_consulta(dados):
    consulta_existe = Consulta.query.filter_by(cpf_fk=dados["cpf"]).first()
    if consulta_existe:
        return False   

    nova_consulta = Consulta(
        cpf_fk=dados.get("cpf"),
        crm_fk=dados.get("crm"),
        data=dados.get("data"),
        horario=dados.get("horario"),
        cidade_fk=dados.get("cidade"),
        especialidade_fk=dados.get("especialidade"),
        hospital_fk=dados.get("hospital"),
    )

    db.session.add(nova_consulta)
    db.session.commit()
    return True

def consulta_agendada(cpf):
    consulta = Consulta.query.filter_by(cpf_fk=cpf).first()
    if not consulta:
        return None 

    usuario = Usuario.query.get(cpf)
    medico = Medico.query.get(consulta.crm_fk)
    hospital = Hospital.query.get(consulta.hospital_fk)
    cidade = Cidade.query.get(consulta.cidade_fk)
    especialidade = Especialidade.query.get(consulta.especialidade_fk)

    informacoes = {
        "hospital": hospital.hospital,
        "endereco": hospital.endereco,
        "cidade": cidade.cidade,
        "especialidade": especialidade.especialidade,
        "cpf": usuario.cpf,
        "medico": medico.nome,
        "crm": medico.crm,
        "horario": consulta.horario,
        "data": consulta.data
    }

    return informacoes


def cancelar_consulta(cpf):
    consulta = Consulta.query.filter_by(cpf_fk=cpf).first()   
    if not consulta:
        return False
    db.session.delete(consulta)
    db.session.commit()
    return True
