from flask import Flask, render_template_string, request, redirect
import views
from utils import *

init_db()

app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    note_id = request.form['id']
    delete_note(note_id)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return views.not_found(error)

if __name__ == '__main__':
    app.run(debug=True)