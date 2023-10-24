# -*- coding: utf-8 -*-
import json
import requests


url = 'http://127.0.0.1:5000/tts'

input_parameters = {

    'text': 'Bienvenidos al Centro Nacional de Seguridad Cibernética .\
de la República de Corea se llevó a cabo a las 10:00 am del día 15 en el Gran Auditorio de la Universidad Femenina Ewha, Seodaemun-gu, Seúl. Unas 2.000 personas participaron en el evento, incluidas sucursales patrióticas, patriotas de la independencia y familias en duelo, personal nacional importante, partidos políticos, representantes del fin de la península de Corea, cuerpo diplomático en Corea, representantes de varios campos y ciudadanos.\
El año pasado limitamos el número de participantes a unos 300 en consideración al resurgimiento del coronavirus, pero este año hemos vuelto al nivel de 2019 debido a la recuperación normal .\
un gran viaje nacional hacia la libertad, esta ceremonia festiva incluyó ceremonias nacionales, proyecciones de videos temáticos, historia conmemorativa, festivales, representaciones de festivales, promoción de canciones de liberación y cantos de tres banzai ',
    'lang': 'es',
    'gender': 0
}

input_json = json.dumps(input_parameters)

response = requests.post(url, input_json)
print(response.json())


