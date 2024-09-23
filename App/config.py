# config.py
DB_CONFIG = {
    'user': 'root',
    'password': 'P@SSw0rd',
    'host': 'localhost',
    'database': 'prueba'
}

# helpers.py

# Títulos de la aplicación
APP_TITLE = "Visualización de Datos"
INDEX_TITLE = "Personas"
BAR_GRAPH_TITLE = "Gráfico de Barras"
PIE_GRAPH_TITLE = "Gráfico Circular"
# Mensajes
AGE_LABEL = "Edad"
SALARY_LABEL = "Salario"
CITY_LABEL = "Ciudad"
BAR_GRAPH_DESCRIPTION = "Relación entre edad y salario"
PIE_GRAPH_DESCRIPTION = "Distribución por ciudad"
# SQL Queries
SQL_QUERY_PERSONAS = "SELECT * FROM personas"

#OTHERS
PNG= 'png'
UTF8="utf-8"

COLUMNAS = {
    'ID': 0,
    'NOMBRE': 1,
    'EDAD': 2,
    'CIUDAD': 3,
    'SALARIO': 4,
}