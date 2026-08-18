import json

def load_data(nome_arquivo):
    caminho = "static/data/" + nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados

def load_template(nome_arquivo):
    caminho = "static/templates/" + nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        template = arquivo.read()

    return template

def add_note(titulo, detalhes):
    notes = load_data("notes.json")

    nova_nota = {
        "titulo": titulo,
        "detalhes": detalhes
    }

    notes.append(nova_nota)

    caminho = "static/data/notes.json"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(notes, arquivo, ensure_ascii=False, indent=4)