# SF
Scrap Form... 
Es un Script en Python para scrapear todos los registros de una web en particular. 
Para esto, utilizaremos bibliotecas como requests y BeautifulSoup. 
Además, si la paginación se maneja a través de parámetros en la URL, podemos automatizar la navegación por todas las páginas.

Primero, asegúrate de tener instaladas las bibliotecas necesarias:
pip install requests beautifulsoup4

Notas:

URL y Paginación: Este script asume que la URL para cada página sigue el formato http://TU-DOMINIO/?pagina={numero}. 
Necesitas ajustar esto según el formato real de la paginación en tu sitio.
Estructura HTML: Asegúrate de que los selectores de BeautifulSoup (find, find_all) coincidan con la estructura HTML de tu página. 
Puedes inspeccionar el HTML con las herramientas de desarrollador del navegador para ajustar estos selectores.
Condición de Parada: La condición de parada del bucle while está basada en el número total de registros dividido por el tamaño de página. Si la web tiene una señal clara de que no hay más páginas, puedes ajustar esta lógica para detectarlo adecuadamente.
Prueba este script y ajusta según sea necesario.
El Resultado lo guarda en registros.csv
