import requests
from bs4 import BeautifulSoup
import pandas as pd

# Configuración inicial
base_url = 'http://ACA-TU-URL/'
data = []

# Función para extraer datos de una página
def extract_data_from_page(page_number):
    url = f'{base_url}?page={page_number}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra la tabla en la página
    table = soup.find('table')  # Ajusta esto según la estructura HTML de la página
    rows = table.find_all('tr')[1:]  # Asumiendo que la primera fila es el encabezado

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)

# Itera sobre todas las páginas
page_number = 1
while True:
    extract_data_from_page(page_number)
    page_number += 1

    # Condición de parada: ajustar según cómo la página indique el final de la paginación
    # Esto puede ser adaptado si hay algún mensaje o ausencia de contenido para detectar el final
    if page_number > 391:  # Suponiendo 100 registros por página para 50000 registros
        break

# Guardar los datos en un archivo CSV
df = pd.DataFrame(data, columns=['NroDoc', 'Apellido y Nombre', 'Correo', 'Celular'])
df.to_csv('registros.csv', index=False)

print("Scraping completado. Datos guardados en 'registros.csv'.")
