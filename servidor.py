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

@app.route("/delete", methods=["POST"])
def delete():
    note_id = request.form["id"]
    delete_note(note_id)
    return redirect("/")

@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit(note_id):
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        edit_note(note_id, title, content)

        return redirect("/")

    note = get_note(note_id)

    if note is None:
        return "Nota não encontrada", 404

    edit_template = load_template("edit.html")

    return render_template_string(edit_template, note=note)

@app.errorhandler(404)
def page_not_found(error):
    return views.not_found(error)

if __name__ == '__main__':
    app.run(debug=True)