#  Esse arquivo e criado as consultas do Banco de Dados
from .models import db, Cidade, Hospital, Especialidade, Medico, HorarioSemana
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
    print(especialistas)
    lista_id = [e.id for e in especialistas]
    return lista_especialista, lista_id

def informacoes_medicas(especialista_id,hospital_id):
    especialista = Especialidade.query.get(especialista_id)
    medico = Medico.query.filter_by(especialidade_fk = especialista_id).first()
    hospital = Hospital.query.get(hospital_id)
    horario_da_semana = HorarioSemana.query.filter_by(medico_fk=medico.crm).first()
    return especialista, medico, hospital, horario_da_semana


