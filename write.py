import json

def confirmar_consulta(dados):
    caminho_arquivo = "txt/consultas.txt"

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha_corrigida = linha.strip()
            if not linha_corrigida:
                continue
            usuario = json.loads(linha_corrigida)              
            if usuario.get("cpf") == dados.get("cpf"):
                return False

    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(json.dumps(dados, ensure_ascii=False) + "\n")
    return True

def cadastra_usuario(dados):
    caminho_arquivo = "txt/usuarios_cadastrados.txt"

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for i, linha in enumerate(arquivo):
            linha_corrigida = linha.strip()
            if not linha_corrigida:
                continue
            usuario = json.loads(linha_corrigida) 
            if usuario.get("cpf") == dados.get("cpf"):
                print(f"CPF {dados['cpf']} já cadastrado!")
                return False  

    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(json.dumps(dados, ensure_ascii=False) + "\n")
        print(f"Usuário {dados['cpf']} cadastrado com sucesso")

    return True


def fazer_login(dados):  
    caminho_arquivo = "txt/usuarios_cadastrados.txt" 
    
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            usuario = json.loads(linha) 
            print(f"Usuário convertido: {usuario}")           
            if usuario["cpf"] == dados["cpf"] and usuario["senha"] == dados["senha"]:
                info = {
                    "nome": usuario["nome"],
                    "cpf": usuario["cpf"],
                    "data": usuario["dataNascimento"],
                    "telefone": usuario["telefone"]
                }           
                return info    
    return {}  


def consultas_agendadas(dados):
    caminho_arquivo = "txt/consultas.txt"

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha_corrigida = linha.strip()
            if not linha_corrigida:
                continue
            usuario = json.loads(linha_corrigida)              
            if usuario.get("cpf") == dados.get("cpf"):
                return usuario
    return False

def autenticar(cpf, senha):
    info = fazer_login({"cpf": cpf, "senha": senha})
    return bool(info)




