import requests

class ServerService:
    def create(self, data):
        # TODO: 
        # - Pasar url a las variables de entorno
        #   Tips: el nombre tiene que se descriptivo por ejemplo: API_URL, lo unico que va a cambiar es el base URL, solo debemos guardar eso.
        # - Pasar el Token a las variables de entorno
        #   Tips: el nombre debe ser descriptivo, por ejemplo: API_TOKEN
        requests.post(url='http://127.0.0.1:8000/servers/', data=data, headers={ 'X-TOKEN': 'token' })
