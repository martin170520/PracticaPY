import requests

def obtener_clima(ciudad, pais):

    '''api_key = 'TU_API_KEY'  # Reemplaza 'TU_API_KEY' con tu clave de API'''

    url = f'https://my-json-server.typicode.com/martin170520/dbClima/db'
    
    try:
        response = requests.get(url)
        datos_clima = response.json()

        temperatura = datos_clima['main']['temp']
        descripcion = datos_clima['weather'][0]['description']

        return temperatura, descripcion
    except Exception as e:
        print(f"Error al obtener el clima: {e}")
        return None, None

# Ejemplo de uso
ciudad = 'Lima'
pais = 'PE'
temperatura, descripcion = obtener_clima(ciudad, pais)
if temperatura is not None and descripcion is not None:
    print(f'El clima en {ciudad}, {pais} es de {temperatura}°C y está {descripcion}.')
else:
    print('No se pudo obtener el clima.')




