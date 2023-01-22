import requests
import json


cidade = 'belo horizonte'
endereco_api = 'http://api.openweathermap.org/data/2.5/weather?appid=051f61db0421b144431738d8c0194744&q='
url = endereco_api + cidade

infos = requests.get(url).json()

# Esse menos 273.15 é porque a informação
# vem em Kelvin e queremos em Celsius
tempo = infos['main']['temp'] - 273.15

humidade = infos['main']['humidity']  # Vem em porcentagem portanto, OK!

temp_maxima = infos['main']['temp_max'] - \
    273.15  # vem em Kelvin e queremos em Celsius
temp_minima = infos['main']['temp_min'] - \
    273.15  # vem em Kelvin e queremos em Celsius

vento_velocidade = infos['wind']['speed']  # vem em Km/h
vento_direcao = infos['wind']['deg']  # Recebe em graus(bussola)]
ceu = infos['clouds']['all']

id_da_cidade = infos['id']

# return tempo, humidade, temp_maxima, temp_minima, vento_velocidade, vento_direcao, id_da_cidade
