# arquivo Seed.py
from .models import db, Cidade, Hospital, Especialidade, Medico, HorarioSemana
from .init import db

def preencher_table():
    # ---------------------- Cidade ----------------------
    if not Cidade.query.first():
        cidades = [
            Cidade(cidade="Picos"), # 1
            Cidade(cidade="Floriano"), # 2 
            Cidade(cidade="Teresina"), # 3
            Cidade(cidade="Parnaíba"), # 4
        ]
        db.session.add_all(cidades)

    # ---------------------- Hospital ----------------------
    if not Hospital.query.first():
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
    if not Especialidade.query.first():
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

    # ---------------------- Medicos ----------------------
    if not Medico.query.first():
        medico = [
            # Medicos do Hospital Regional - Picos
            Medico(
                crm="123456",
                especialidade_fk=1,  
                nome="Dr. João Silva",
                texto="Sou Dr. João Silva, Clínico Geral formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 1
            Medico(
                crm="234567",
                especialidade_fk=2,  
                nome="Dra. Maria Souza",
                texto="Sou Dra. Maria Souza, Cardiologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 2
            Medico(
                crm="345678",
                especialidade_fk=3,  
                nome="Dr. Carlos Lima",
                texto="Sou Dr. Carlos Lima, Ginecologista formado em Medicina formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 3

            # Medicos da UPA 24h - Picos
            Medico(
                crm="567890",
                especialidade_fk=4,  
                nome="Dra. Fernanda Costa",
                texto="Sou Dra. Fernanda Costa, Ortopedista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 4
            Medico(
                crm="723956",
                especialidade_fk=5,  
                nome="Dr. Eduardo Lima",
                texto="Sou Dr. Eduardo Lima, Clínico Geral formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 5
            Medico(
                crm="223458",
                especialidade_fk=6,  
                nome="Dr. Rafael Santos",
                texto="Sou Dr. Rafael Santos, Dermatologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 6

            # Medicos do Hospital do Monte Castelo - Teresina
            Medico(
                crm="323456",
                especialidade_fk=7,  
                nome="Dra. Beatriz Costa",
                texto="Sou Dra. Beatriz Costa, Pediatra formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 7
            Medico(
                crm="523457",
                especialidade_fk=8,  
                nome="Dr. Pedro Almeida",
                texto="Sou Dr. Pedro Almeida, Clínico Geral formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 8
            Medico(
                crm="423456",
                especialidade_fk=9,  
                nome="Dr. Tiago Fernandes",
                texto="Sou Dr. Tiago Fernandes, Dermatologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 9

            # Medicos da UPA - Floriano
            Medico(
                crm="623457",
                especialidade_fk=10,  
                nome="Dr. André Carvalho",
                texto="Sou Dr. André Carvalho, Neurologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 10
            Medico(
                crm="723459",
                especialidade_fk=11,  
                nome="Dr. Samuel Pinto",
                texto="Sou Dr. Samuel Pinto, Cardiologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 11

            # Medicos de Hospital do Monte Castelo - Teresina (corrigido nome e CRM repetidos)
            Medico(
                crm="725558",
                especialidade_fk=12,
                nome="Dr. Lucas Barros",
                texto="Sou Dr. Lucas Barros, Cardiologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 12

            Medico(
                crm="823451",
                especialidade_fk=13,
                nome="Dra. Helena Moura",
                texto="Sou Dra. Helena Moura, especialista em Clínica Geral formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 13

            Medico(
                crm="932874",
                especialidade_fk=14,
                nome="Dr. Marcos Vieira",
                texto="Sou Dr. Marcos Vieira, Dermatologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 14

            # Medicos do Hospital Santa Maria - Teresina
            Medico(
                crm="748392",
                especialidade_fk=15,
                nome="Dr. Rodrigo Nascimento",
                texto="Sou Dr. Rodrigo Nascimento, Clínico Geral formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 15

            Medico(
                crm="582931",
                especialidade_fk=16,
                nome="Dra. Camila Araújo",
                texto="Sou Dra. Camila Araújo, Cardiologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
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
                texto="Sou Dr. André Fagundes, Cardiologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 19

            Medico(
                crm="437912",
                especialidade_fk=20,
                nome="Dra. Rafaela Fontes",
                texto="Sou Dra. Rafaela Fontes, Neurologista formado em Medicina pela Universidade Federal UF no ano de 2025. Atuo com foco na prevenção, tratamento e orientação à saúde, buscando sempre o bem-estar físico e emocional de cada paciente. Atualmente, realizo atendimentos no Hospital São Lucas, onde ofereço consultas voltadas à avaliação geral de saúde."
            ), # 20
        ]
        db.session.add_all(medico)

    if not HorarioSemana.query.first():
        horario_da_semana =[
            HorarioSemana(
                medico_fk="123456",
                segunda="08:00,09:00,10:00,11:00",
                terca="08:00,09:00,10:00",
                quarta="08:00,09:00,11:00,15:00",
                quinta="",
                sexta="08:00,14:00",
                sabado="",
                domingo="08:00,09:00,10:00",
            ),# 1
            HorarioSemana(
                medico_fk="234567",
                segunda="07:00,08:00,09:00",
                terca="07:00,09:00,11:00",
                quarta="08:00,10:00",
                quinta="08:00,09:00",
                sexta="07:00,10:00",
                sabado="",
                domingo="",
            ),# 2
            HorarioSemana(
                medico_fk="345678",
                segunda="13:00,14:00,15:00",
                terca="14:00,15:00",
                quarta="13:00,16:00",
                quinta="14:00,15:00,16:00",
                sexta="13:00",
                sabado="",
                domingo="",
            ),# 3
            HorarioSemana(
                medico_fk="567890",
                segunda="",
                terca="09:00,10:00",
                quarta="09:00",
                quinta="09:00,11:00",
                sexta="10:00,11:00",
                sabado="",
                domingo="08:00,09:00",
            ),# 4
            HorarioSemana(
                medico_fk="723956",
                segunda="08:00,09:00",
                terca="10:00,11:00",
                quarta="",
                quinta="08:00,10:00",
                sexta="09:00,10:00,11:00",
                sabado="08:00",
                domingo="",
            ), # 5
            HorarioSemana(
                medico_fk="323456",
                segunda="07:00,08:00",
                terca="07:00,08:00,09:00",
                quarta="07:00",
                quinta="",
                sexta="07:00,08:00,09:00,10:00",
                sabado="",
                domingo="",
            ),# 6
            HorarioSemana(
                medico_fk="523457",
                segunda="13:00,14:00",
                terca="13:00,15:00",
                quarta="14:00",
                quinta="13:00,14:00",
                sexta="",
                sabado="14:00,15:00",
                domingo="",
            ), # 7
            HorarioSemana(
                medico_fk="423456",
                segunda="",
                terca="",
                quarta="10:00,11:00",
                quinta="09:00,10:00",
                sexta="09:00,11:00",
                sabado="",
                domingo="09:00",
            ), # 8
            HorarioSemana(
                medico_fk="423456",
                segunda="08:00,10:00",
                terca="08:00",
                quarta="08:00,09:00,10:00",
                quinta="",
                sexta="10:00,11:00,12:00",
                sabado="08:00,09:00",
                domingo="",
            ),# 9
            HorarioSemana(
                medico_fk="723459",
                segunda="14:00,15:00",
                terca="13:00,14:00,15:00",
                quarta="",
                quinta="15:00,16:00",
                sexta="14:00",
                sabado="15:00",
                domingo="",
            ), # 10
            HorarioSemana(
                medico_fk="723459",
                segunda="08:00,09:00,10:00",
                terca="09:00,10:00,11:00",
                quarta="08:00,09:00",
                quinta="10:00,11:00",
                sexta="08:00,09:00,10:00",
                sabado="",
                domingo=""
            ), # 12
            HorarioSemana(
                medico_fk="823451",
                segunda="07:00,08:00",
                terca="08:00,09:00",
                quarta="07:00,08:00",
                quinta="07:00,08:00,09:00",
                sexta="07:00,08:00",
                sabado="09:00,10:00",
                domingo=""
            ), # 13
            HorarioSemana(
                medico_fk="932874",
                segunda="13:00,14:00,15:00",
                terca="14:00,15:00",
                quarta="13:00,14:00",
                quinta="14:00,15:00",
                sexta="13:00,14:00",
                sabado="",
                domingo=""
            ), # 14
            HorarioSemana(
                medico_fk="748392",
                segunda="08:00,09:00",
                terca="08:00,09:00,10:00",
                quarta="09:00,10:00",
                quinta="08:00,09:00",
                sexta="08:00,09:00",
                sabado="08:00",
                domingo=""
            ), # 15
            HorarioSemana(
                medico_fk="582931",
                segunda="07:00,08:00",
                terca="07:00,08:00",
                quarta="07:00,08:00",
                quinta="07:00,08:00",
                sexta="07:00,08:00",
                sabado="",
                domingo=""
            ), # 16
            HorarioSemana(
                medico_fk="101010",
                segunda="10:00,11:00",
                terca="10:00,11:00",
                quarta="10:00,11:00",
                quinta="10:00,11:00",
                sexta="10:00,11:00",
                sabado="",
                domingo=""
            ),
            HorarioSemana(
                medico_fk="691245",
                segunda="08:00,09:00,10:00,11:00",
                terca="08:00,09:00,10:00",
                quarta="08:00,09:00",
                quinta="08:00,09:00",
                sexta="08:00,09:00",
                sabado="08:00,09:00",
                domingo=""
            ), # 17
            HorarioSemana(
                medico_fk="519283",
                segunda="07:00,08:00,09:00",
                terca="07:00,08:00",
                quarta="07:00,08:00,09:00",
                quinta="08:00,09:00",
                sexta="07:00,08:00",
                sabado="07:00,08:00",
                domingo=""
            ), # 18
            HorarioSemana(
                medico_fk="873210",
                segunda="13:00,14:00",
                terca="13:00,14:00",
                quarta="13:00,14:00",
                quinta="13:00,14:00",
                sexta="13:00,14:00",
                sabado="13:00",
                domingo=""
            ), # 19
            HorarioSemana(
                medico_fk="437912",
                segunda="08:00,09:00,10:00",
                terca="09:00,10:00,11:00",
                quarta="08:00,09:00,10:00",
                quinta="08:00,09:00",
                sexta="08:00,09:00,10:00",
                sabado="08:00,09:00",
                domingo=""
            ) # 20
        ]
        db.session.add_all(horario_da_semana)
   
    db.session.commit()
