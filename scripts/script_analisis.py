import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuración de rutas relativas profesionales
DIRECCION_BASE = os.path.dirname(os.path.abspath(__file__))
RUTA_DATOS = os.path.join(DIRECCION_BASE, '..', 'datos', 'datos_climaticos.csv')
RUTA_RESULTADOS = os.path.join(DIRECCION_BASE, '..', 'resultados')
# ... (aquí sigue todo el resto del código que te pasé antes)

# Asegurar que exista la carpeta de salida para los gráficos
os.makedirs(RUTA_RESULTADOS, exist_ok=True)

def cargar_y_procesar_datos():
    print("PROY-2: feat: Iniciando procesamiento de datos climáticos/iris...")

    # Nombres de columnas adaptados al formato del dataset real
    columnas = [
        'Temperatura_Media_Anual',  # sepal length
        'Variabilidad_Mensual',    # sepal width
        'Indice_Precipitacion',    # petal length
        'Presion_Atmosferica',     # petal width
        'Region_Pais'              # class
    ]

    # URL de respaldo o lectura directa del archivo descargado
    url_datos = "https://uci.edu"

    try:
        # Intenta leer local, si no, descarga directamente de la URL oficial
        if os.path.exists(RUTA_DATOS):
            df = pd.read_csv(RUTA_DATOS, header=None, names=columnas)
            print("Datos cargados desde el repositorio local.")
        else:
            df = pd.read_csv(url_datos, header=None, names=columnas)
            print("Datos descargados exitosamente desde UCI Archive.")
    except Exception as e:
        print(f"PROY-2: error: Falló la carga de datos: {e}")
        return

    # Limpieza de etiquetas de regiones/países (eliminar el prefijo 'Iris-')
    df['Region_Pais'] = df['Region_Pais'].str.replace('Iris-', '').str.capitalize()

    # 2. Análisis Estadístico Descriptivo (Agrupado por Región/País)
    print("\n--- RESUMEN ESTADÍSTICO POR REGIÓN ---")
    resumen = df.groupby('Region_Pais')['Temperatura_Media_Anual'].describe()
    print(resumen)

    # Guardar reporte estadístico en formato de texto
    ruta_reporte = os.path.join(RUTA_RESULTADOS, 'reporte_estadistico.txt')
    resumen.to_string(ruta_reporte)
    print(f"\nReporte estadístico guardado en: {ruta_reporte}")

    # 3. Generación de Gráficos de Tendencia
    plt.figure(figsize=(10, 6))

    # Crear un Boxplot de la variable principal agrupada por región
    df.boxplot(column='Temperatura_Media_Anual', by='Region_Pais', grid=False, patch_artist=True)

    plt.title('Distribución de Temperatura Media Anual por Región')
    plt.suptitle('')  # Eliminar título automático de pandas
    plt.xlabel('Región / País')
    plt.ylabel('Temperatura Promedio (°C)')

    # Guardar gráfico de forma automática
    ruta_grafico = os.path.join(RUTA_RESULTADOS, 'analisis_temperaturas.png')
    plt.savefig(ruta_grafico, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Gráfico analítico exportado en: {ruta_grafico}")
    print("PROY-2: feat: Script finalizado con éxito.")

if __name__ == "__main__":
    cargar_y_procesar_datos()
