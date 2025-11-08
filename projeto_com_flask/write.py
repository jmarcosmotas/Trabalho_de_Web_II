import json

def confirmar_consulta(dados):
    caminho_arquivo = "txt/consultas.txt"  
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{dados}") 

def cadastra_usuario(dados):
    caminho_arquivo = "txt/usuarios_cadastrados.txt"  
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{dados}")


import json

def fazer_login(dados):
    print(f"Dados recebidos para login: {dados}")
    
    caminho_arquivo = "txt/usuarios_cadastrados.txt" 
    
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            print(f"Linha lida do arquivo: {linha.strip()}")

            linha_corrigida = linha.replace("'", '"')

            usuario = json.loads(linha_corrigida) 
            print(f"Usuário convertido: {usuario}")           
            if usuario["cpf"] == dados["cpf"] and usuario["senha"] == dados["senha"]:
                print(f"Login bem-sucedido para o CPF: {usuario['cpf']}")
                info = {
                    "nome": usuario["nome"],
                    "cpf": usuario["cpf"],
                    "data": usuario["dataNascimento"],
                    "telefone": usuario["telefone"]
                }
            
                return info  
    
    return {}  




