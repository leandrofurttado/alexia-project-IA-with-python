import requests
from bs4 import BeautifulSoup

req = requests.get('https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F015fr&state=7&gl=BR&ceid=BR%3Apt-419')

soupvacination = BeautifulSoup(req.text, 'html.parser')

porcentagem_vacina = soupvacination.findAll("div", {"class": "tIUMlb"})
pessoas_vacinadas = soupvacination.find("div", {"class": "UvMayb"})

porcentagem = porcentagem_vacina[3].strong.text
pessoas = pessoas_vacinadas.text
