# app.py
from flask import Flask, render_template
from db import Database
from logic import BusinessLogic
from config import APP_TITLE, INDEX_TITLE, BAR_GRAPH_TITLE, PIE_GRAPH_TITLE

app = Flask(__name__, template_folder='templates')

# Instanciamos las clases
db = Database()
logic = BusinessLogic()

@app.route('/')
def index():
    # Conectar a la base de datos
    db.connect()
    logic = BusinessLogic()

    # Obtener los datos
    personas = db.get_personas()

    # Generar gráficos
    grafico_barra = logic.generar_grafico_barras(personas)
    imagen_barra = logic.convertir_figura_a_base64(grafico_barra)

    grafico_circular = logic.generar_grafico_circular(personas)
    imagen_circular = logic.convertir_figura_a_base64(grafico_circular)

    # Cerrar la conexión a la base de datos
    db.close()

    # Renderizar la plantilla
    return render_template('index.html', 
                           personas=personas, 
                           app_title=APP_TITLE, 
                           index_title=INDEX_TITLE, 
                           bar_graph_title=BAR_GRAPH_TITLE, 
                           pie_graph_title=PIE_GRAPH_TITLE, 
                           imagen_barra=imagen_barra, 
                           imagen_circular=imagen_circular)

if __name__ == '__main__':
    app.run(debug=True)
