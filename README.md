
# Visualización de Datos con Flask, MySQL y Matplotlib

Este proyecto es una aplicación web simple desarrollada con Flask, que se conecta a una base de datos MySQL para extraer datos de personas y visualiza esta información mediante gráficos generados con Matplotlib. Los gráficos incluyen un gráfico de barras y un gráfico circular, ambos presentados en una página HTML.

## Estructura del Proyecto

La estructura del proyecto es modular y organizada para facilitar el mantenimiento y la extensibilidad. Cada componente (conexión a la base de datos, lógica de negocio, presentación) está separado en archivos individuales.

```
App
.
├── app.py                 # Aplicación principal de Flask
├── db.py                  # Clase para la conexión a la base de datos MySQL
├── logic.py               # Clase para la lógica de negocio (gráficos)
├── helpers.py             # Archivo que contiene cadenas de texto y consultas SQL
├── config.py              # Archivo de configuración para la base de datos
├── templates
│   └── index.html         # Plantilla HTML para la visualización de datos
└── README.md              # Documentación del proyecto
```

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- MySQL
- Flask
- Matplotlib
- Plotly
- SQLAlchemy
- MySQL Connector

Puedes instalar las dependencias necesarias utilizando el siguiente comando:

```bash
pip install flask matplotlib mysql-connector-python SQLAlchemy plotly
```

## Configuración de la Base de Datos

Este proyecto se conecta a una base de datos MySQL. Debes configurar la conexión en el archivo `config.py`.

### Ejemplo de `config.py`:

```python
# config.py
DB_CONFIG = {
    'user': 'root',
    'password': 'P@SSw0rd',
    'host': 'localhost',
    'database': 'prueba'
}
```

Asegúrate de que los valores coincidan con tu configuración local de MySQL.

## Uso de las Clases

### 1. `db.py`: Clase de Conexión a la Base de Datos
Esta clase gestiona la conexión a la base de datos y ejecuta consultas.

- `Database.connect()`: Conecta a la base de datos.
- `Database.fetch_personas()`: Ejecuta una consulta SQL para obtener los datos de la tabla `personas`.
- `Database.close()`: Cierra la conexión a la base de datos.

### 2. `logic.py`: Lógica de Negocio
Esta clase contiene la lógica para generar gráficos basados en los datos obtenidos de la base de datos. También gestiona la limpieza de gráficos en memoria.

- `BusinessLogic.generar_grafico_barras(personas)`: Genera un gráfico de barras basado en los datos de las personas.
- `BusinessLogic.generar_grafico_circular(personas)`: Genera un gráfico circular para mostrar la distribución de las ciudades.
- `BusinessLogic.convertir_figura_a_base64(fig)`: Convierte una figura de Matplotlib en una cadena de base64 para su inclusión en HTML.
- `BusinessLogic.clear_graphics()`: Limpia los gráficos en memoria antes de generar nuevos.

### 3. `helpers.py`: Archivo de Utilidades
Aquí se almacenan todas las cadenas de texto y consultas SQL para facilitar la gestión del código.

- Títulos de gráficos y etiquetas
- Consultas SQL (`SQL_QUERY_PERSONAS`)

## Estructura del Frontend

El archivo `templates/index.html` contiene la plantilla HTML donde se muestran los datos y gráficos.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ app_title }}</title>
</head>
<body>
    <h1>{{ index_title }}</h1>
    <table border="1">
        <tr>
            <th>Nombre</th>
            <th>Edad</th>
            <th>Ciudad</th>
            <th>Salario</th>
        </tr>
        {% for persona in personas %}
        <tr>
            <td>{{ persona[1] }}</td>
            <td>{{ persona[2] }}</td>
            <td>{{ persona[3] }}</td>
            <td>{{ persona[4] }}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>{{ bar_graph_title }}</h2>
    <img src="data:image/png;base64,{{ fig1 }}"/>

    <h2>{{ pie_graph_title }}</h2>
    <img src="data:image/png;base64,{{ fig2 }}"/>
</body>
</html>
```

## Ejecución del Proyecto

1. Asegúrate de que la base de datos esté en funcionamiento y que los datos estén en la tabla `personas`.

2. Ejecuta el archivo `app.py` para iniciar el servidor Flask:

```bash
python app.py
```

3. Abre tu navegador y navega a `http://127.0.0.1:5000/` para ver la aplicación en funcionamiento.

## Base de Datos

Este proyecto asume que tienes una base de datos MySQL llamada `prueba` con una tabla llamada `personas`. A continuación se muestra un ejemplo de la estructura de la tabla:

```sql
Create Database	Prueba;
CREATE TABLE `prueba`.`personas` (
  personaspersonas`id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `edad` INT NULL,
  `ciudad` VARCHAR(45) NULL,
  `salario` DECIMAL NULL,
  PRIMARY KEY (`id`));

INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('1', 'CHRISTIAN', '20', 'LIMA', '7500');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('2', 'ALEX', '25', 'LIMA', '3500');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('3', 'MARIA', '40', 'PIURA', '5849');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('4', 'JUANA', '35', 'CAJAMARCA', '3045');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('5', 'ELIZABETH', '30', 'LIMA', '2345');
```

Llena la tabla con algunos datos para ver la visualización en la página principal.

## Personalización

Puedes personalizar varios aspectos del proyecto:

- **Base de datos**: Cambia las credenciales y el nombre de la base de datos en `config.py`.
- **Cadenas de texto**: Actualiza los títulos y etiquetas en `helpers.py`.
- **Gráficos**: Modifica las funciones en `logic.py` para generar otros tipos de gráficos según tus necesidades.

## Consideraciones de Desempeño

- Se utiliza `plt.cla()` y `plt.clf()` en la clase `BusinessLogic` para asegurarse de que los gráficos generados previamente sean limpiados y no ocupen memoria innecesariamente.
- Para mejorar la escalabilidad, podrías implementar caché en la aplicación para evitar consultas repetitivas a la base de datos si los datos no cambian con frecuencia.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Añadí una nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes ver más detalles en el archivo `LICENSE`.
