from utils import load_data, load_template, save_note

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(
            id=dados['id'],
            title=dados['title'],
            details=dados['content'],
            favorite_class='favorite' if dados.get('favorite', 0) else '',
            favorite_icon='★' if dados.get('favorite', 0) else '☆',
            favorite_label='Desfavoritar' if dados.get('favorite', 0) else 'Favoritar'
        )
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    nova_anotacao = {"titulo": titulo, "detalhes": detalhes}
    save_note(nova_anotacao)

def not_found(error):
    return "Página não encontrada", 404