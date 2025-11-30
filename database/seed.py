from .models import db, Cidade, Hospital, Especialidade, Medico
from .init import db

def preencher_table():
    # ---------------------- Cidade ----------------------
    cidades = [
        Cidade(cidade="Picos"), # 1
        Cidade(cidade="Floriano"), # 2 
        Cidade(cidade="Teresina"), # 3
        Cidade(cidade="Parnaíba"), # 4
    ]

    db.session.add_all(cidades)


    # ---------------------- Hospital ----------------------

    hospital = [
        # Hospital de Picos
        Hospital(cidade_fk=1, hospital="Hospital Regional De Picos", endereco="Praça Antenor Neiva, 184 - Bomba"), # 1
        Hospital(cidade_fk=1, hospital="UPA 24h - Picos", endereco="R. Joaquim Pacifico da Silva - Catavento"), # 2
        # Hospital de Floriano 
        Hospital(cidade_fk=2, hospital="Hospital Regional Tibério Nunes", endereco="R. Gabriel Ferreira, S/N - Manguinha"), # 3
        Hospital(cidade_fk=2, hospital="UPA - Floriano", endereco="R. João Justino - Matadouro"), # 4
        # Hospital de Teresina
        Hospital(cidade_fk=3, hospital="Hospital do Monte Castelo", endereco="R. Antônio Cavour de Miranda, 357 - Monte Castelo"), # 5
        Hospital(cidade_fk=3, hospital="Hospital Santa Maria", endereco="Rua Governador Raimundo Artur de Vasconcelos, 616 - Centro (Sul)"), # 6
        # Hostital de Paraiba
        Hospital(cidade_fk=4, hospital="Hospital Estadual Dirceu Arcoverde", endereco="R. Rodrigues Coimbra, 1650 - Rodoviária") # 7
    ]

    db.session.add_all(hospital)


    # ---------------------- Especialidade ----------------------
    especialidades = [
        # Especilidade do Hospital Regional - Picos
        Especialidade(hospital_fk=1, especialidade="Clínico Geral"), # 1 
        Especialidade(hospital_fk=1, especialidade="Cardiologia"), # 2 
        Especialidade(hospital_fk=1, especialidade="Ginecologia"), # 3 

        # Especilidade da UPA 24h - Picos
        Especialidade(hospital_fk=2, especialidade="Ortopedia"), # 4
        Especialidade(hospital_fk=2, especialidade="Clínico Geral"), # 5
        Especialidade(hospital_fk=2, especialidade="Dermatologia"), # 6

        # Especilidade do Hospital Regional Tibério Nunes - Floriano
        Especialidade(hospital_fk=3, especialidade="Pediatria"), # 7
        Especialidade(hospital_fk=3, especialidade="Clínico Geral"), # 8
        Especialidade(hospital_fk=3, especialidade="Dermatologia"), # 9

        # Especialidade da UPA - Floriano
        Especialidade(hospital_fk=4, especialidade="Neurologia"), # 10
        Especialidade(hospital_fk=4, especialidade="Cardiologia"), # 11

        # Especialidade Hospital do Monte Castelo - Teresina
        Especialidade(hospital_fk=5, especialidade="Cardiologia"), # 12
        Especialidade(hospital_fk=5, especialidade="Clínico Geral"), # 13
        Especialidade(hospital_fk=5, especialidade="Dermatologia"), # 14

        # Especialidade do Hospital Santa Maria - Teresinar 
        Especialidade(hospital_fk=6, especialidade="Clínico Geral"), # 15
        Especialidade(hospital_fk=6, especialidade="Cardiologia"), # 16
        Especialidade(hospital_fk=6, especialidade="Ortopedia"), # 17

        # Especialidade do Hospital Estadual Dirceu Arcoverde - Parnaiba
        Especialidade(hospital_fk=7, especialidade="Dermatologia"), # 18
        Especialidade(hospital_fk=7, especialidade="Cardiologia"), # 19
        Especialidade(hospital_fk=7, especialidade="Neurologia"), # 20
    ]

    db.session.add_all(especialidades)
    db.session.commit()

    medico = [

        # Medicos do Hospital Regional - Picos
        Medico(
            crm="123456",
            especialidade_fk=1,  
            nome="Dr. João Silva",
            texto="Sou Dr. João Silva, Clínico Geral formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 1
        Medico(
            crm="234567",
            especialidade_fk=2,  
            nome="Dra. Maria Souza",
            texto="Sou Dra. Maria Souza, Cardiologista formada em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 2
        Medico(
            crm="345678",
            especialidade_fk=3,  
            nome="Dr. Carlos Lima",
            texto="Sou Dr. Carlos Lima, Ginecologista formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 3

        # Medicos da UPA 24h - Picos
        Medico(
            crm="567890",
            especialidade_fk=4,  
            nome="Dra. Fernanda Costa",
            texto="Sou Dra. Fernanda Costa, Ortopedista formada em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 4
        Medico(
            crm="723956",
            especialidade_fk=5,  
            nome="Dr. Eduardo Lima",
            texto="Sou Dr. Eduardo Lima, Clínico Geral formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 5
        Medico(
            crm="223458",
            especialidade_fk=6,  
            nome="Dr. Rafael Santos",
            texto="Sou Dr. Rafael Santos, Dermatologista formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 6

        # Medicos do Hospital do Monte Castelo - Teresina
        Medico(
            crm="323456",
            especialidade_fk=7,  
            nome="Dra. Beatriz Costa",
            texto="Sou Dra. Beatriz Costa, Pediatra formada em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 7
        Medico(
            crm="523457",
            especialidade_fk=8,  
            nome="Dr. Pedro Almeida",
            texto="Sou Dr. Pedro Almeida, Clínico Geral formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 8
        Medico(
            crm="423456",
            especialidade_fk=9,  
            nome="Dr. Tiago Fernandes",
            texto="Sou Dr. Tiago Fernandes, Dermatologista formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 9

        # Medicos da UPA - Floriano
        Medico(
            crm="623457",
            especialidade_fk=10,  
            nome="Dr. André Carvalho",
            texto="Sou Dr. André Carvalho, Neurologista formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 10
        Medico(
            crm="723459",
            especialidade_fk=11,  
            nome="Dr. Samuel Pinto",
            texto="Sou Dr. Samuel Pinto, Cardiologista formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 11

        # Medicos de Hospital do Monte Castelo - Teresina (corrigido nome e CRM repetidos)
        Medico(
            crm="725558",
            especialidade_fk=12,
            nome="Dr. Lucas Barros",
            texto="Sou Dr. Lucas Barros, Cardiologista formado em Medicina pela Universidade Federal UF no ano de 2025..."
        ), # 12

        Medico(
            crm="823451",
            especialidade_fk=13,
            nome="Dra. Helena Moura",
            texto="Sou Dra. Helena Moura, especialista em Clínica Geral..."
        ), # 13

        Medico(
            crm="932874",
            especialidade_fk=14,
            nome="Dr. Marcos Vieira",
            texto="Sou Dr. Marcos Vieira, Dermatologista formado pela Universidade Federal UF..."
        ), # 14

        # Medicos do Hospital Santa Maria - Teresina
        Medico(
            crm="748392",
            especialidade_fk=15,
            nome="Dr. Rodrigo Nascimento",
            texto="Sou Dr. Rodrigo Nascimento, Clínico Geral com experiência na saúde do adulto..."
        ), # 15

        Medico(
            crm="582931",
            especialidade_fk=16,
            nome="Dra. Camila Araújo",
            texto="Sou Dra. Camila Araújo, Cardiologista dedicada ao diagnóstico e prevenção..."
        ), # 16

        Medico(
            crm="691245",
            especialidade_fk=17,
            nome="Dr. Thiago Mendonça",
            texto="Sou Dr. Thiago Mendonça, Ortopedista com foco em ossos e articulações..."
        ), # 17

        # Especialidade do Hospital Estadual Dirceu Arcoverde - Parnaiba
        Medico(
            crm="519283",
            especialidade_fk=18,
            nome="Dra. Larissa Monteiro",
            texto="Sou Dra. Larissa Monteiro, Dermatologista, atuando na prevenção e tratamento de doenças cutâneas..."
        ), #18

        Medico(
            crm="873210",
            especialidade_fk=19,
            nome="Dr. André Fagundes",
            texto="Sou Dr. André Fagundes, Cardiologista focado em promover saúde cardiovascular..."
        ), # 19

        Medico(
            crm="437912",
            especialidade_fk=20,
            nome="Dra. Rafaela Fontes",
            texto="Sou Dra. Rafaela Fontes, Neurologista atuando no diagnóstico e tratamento de doenças do sistema nervoso..."
        ), # 20
    ]

    db.session.add_all(medico)
    db.session.commit()
