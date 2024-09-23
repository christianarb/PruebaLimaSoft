# logic.py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import io
from config import COLUMNAS,AGE_LABEL, SALARY_LABEL, BAR_GRAPH_DESCRIPTION, PIE_GRAPH_DESCRIPTION, CITY_LABEL
import numpy as np
class BusinessLogic:
    def __init__(self):
        """Constructor que limpia cualquier gráfico anterior en memoria"""
        self.limpiar_graphics()

    def limpiar_graphics(self):
        """Método para limpiar gráficos en memoria"""
        plt.cla()  # Limpia los ejes actuales
        plt.clf()  # Limpia la figura actual
    
    def generar_grafico_barras(self, personas):
        """Genera un gráfico de barras basado en los datos de personas"""
        self.limpiar_graphics()  # Asegura que no haya gráficos previos en memoria
        edades = [p[COLUMNAS.get("EDAD")] for p in personas]
        salarios = [p[COLUMNAS.get("SALARIO")] for p in personas]
        plt.bar(edades, salarios)
        plt.xlabel(AGE_LABEL)
        plt.ylabel(SALARY_LABEL)
        plt.title(BAR_GRAPH_DESCRIPTION)
        return plt.gcf()  # Devuelve la figura actual   

    def generar_grafico_circular(self, personas):
        """Genera un gráfico circular basado en los datos de personas"""
        self.limpiar_graphics()  # Asegura que no haya gráficos previos en memoria
        ciudades = [p[COLUMNAS.get("CIUDAD")] for p in personas]
        cantidad_ciudades = {}
        
        # Contar la cantidad de personas en cada ciudad
        for ciudad in ciudades:
            if ciudad in cantidad_ciudades:
                cantidad_ciudades[ciudad] += 1
            else:
                cantidad_ciudades[ciudad] = 1
                
        labels = list(cantidad_ciudades.keys())
        valores = list(cantidad_ciudades.values())
        
        # Generar el gráfico circular
        wedges, texts = plt.pie(valores, labels=labels, startangle=90)
        
        for i, wedge in enumerate(wedges):
            # Obtener el ángulo del wedge
            theta = (wedge.theta1 + wedge.theta2) / 2
            x = np.cos(np.radians(theta)) * 0.5  # Ajustar la posición x
            y = np.sin(np.radians(theta)) * 0.5  # Ajustar la posición y
            
            # Obtener el color del wedge
            color_wedge = wedge.get_facecolor()
            
            # Calcular el brillo del color para determinar el color del texto
            brightness = np.sqrt(0.241 * color_wedge[0] ** 2 + 0.691 * color_wedge[1] ** 2 + 0.068 * color_wedge[2] ** 2)
            
            # Establecer color del texto en blanco o negro dependiendo del brillo
            text_color = 'white' if brightness < 0.5 else 'black'

            plt.text(x, y, str(valores[i]), ha='center', va='center', fontsize=12, color=text_color)


        plt.title(PIE_GRAPH_DESCRIPTION)
        plt.axis('equal')  # Asegura que el gráfico circular se dibuje como un círculo
        return plt.gcf()


    def convertir_figura_a_base64(self, fig):
        """Convierte una figura en base64 para su uso en HTML"""
        s1 = io.BytesIO()
        fig.savefig(s1, format='png', bbox_inches="tight")
        pic_hash = base64.b64encode(s1.getvalue()).decode("utf-8").replace("\n", "")
        return pic_hash
