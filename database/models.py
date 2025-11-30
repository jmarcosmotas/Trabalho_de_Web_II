# Arquivo model.py
from .init import db
# ---------------------- Usuario ----------------------
class Usuario(db.Model):
    __tablename__ = "usuario"
    
    cpf = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(14), nullable=False)
    data_n = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# ---------------------- Cidade ----------------------
class Cidade(db.Model):
    __tablename__ = "cidade"
    
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(30), nullable=False)


# ---------------------- Hospital ----------------------
class Hospital(db.Model):
    __tablename__ = "hospital"
    
    id = db.Column(db.Integer, primary_key=True)
    cidade_fk = db.Column(db.Integer, db.ForeignKey("cidade.id"), nullable=False)
    hospital = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)


# ---------------------- Especialidade ----------------------
class Especialidade(db.Model):
    __tablename__ = "especialidade"
    
    id = db.Column(db.Integer, primary_key=True)
    hospital_fk = db.Column(db.Integer, db.ForeignKey("hospital.id"), nullable=False)
    especialidade = db.Column(db.String(50), nullable=False)



# ---------------------- Medico ----------------------
class Medico(db.Model):
    __tablename__ = "medico"
    
    crm = db.Column(db.String(6), primary_key=True)
    especialidade_fk = db.Column(db.Integer, db.ForeignKey("especialidade.id"), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    texto = db.Column(db.String(400), nullable=False)


# ---------------------- Semana ----------------------
class Semana(db.Model):
    __tablename__ = "semana"
    
    id = db.Column(db.Integer, primary_key=True)
    medico_fk = db.Column(db.String(6), db.ForeignKey("medico.crm"), nullable=False)
    dia_semana = db.Column(db.String(10), nullable=False)


# ---------------------- Horario ----------------------
class Horario(db.Model):
    __tablename__ = "horario"
    
    id = db.Column(db.Integer, primary_key=True)
    semana_fk = db.Column(db.Integer, db.ForeignKey("semana.id"), nullable=False)
    horario = db.Column(db.String(5), nullable=False)


# ---------------------- Consulta ----------------------
class Consulta(db.Model):
    __tablename__ = "consulta"
    
    id = db.Column(db.Integer, primary_key=True)
    
    cpf = db.Column(db.String(14), db.ForeignKey("usuario.cpf"), nullable=False)
    crm = db.Column(db.String(6), db.ForeignKey("medico.crm"), nullable=False)
    
    data = db.Column(db.String(10), nullable=False)
    horario = db.Column(db.String(5), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    especialidade = db.Column(db.String(30), nullable=False)
    hospital = db.Column(db.String(30), nullable=False)
