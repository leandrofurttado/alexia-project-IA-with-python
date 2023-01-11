import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from datetime import datetime
import wikipedia
import pywhatkit
import covid_dados
from random import randint
import words_exists
import clima_tempo


wikipedia.set_lang("pt")
hora_atual = datetime.now().strftime("%H")
hora_atual = int(hora_atual)
audio = sr.Recognizer()
fernanda = pyttsx3.init()



## INICIO DA CONVERSA COM A FERNANDA: (APRESENTAÇÃO DO NOME)
#TODO COLOCAR UMA LISTA DE FALAS PARA A FERNANDA FALAR QUANDO INICIAR EX:'' OLA MEU NOME É FERNANDA, COM QUEM EU FALO?''
fernanda.say('Olá meu nome é Fernanda, primeiramente me diga o seu nome ')
fernanda.runAndWait()

todas_as_palavras = words_exists.words

with sr.Microphone() as escutando:
    print('Ouvindo você...')
    voz = audio.listen(escutando)
    nome_usuario = audio.recognize_google(voz, language='pt')
    nome_usuario = nome_usuario.lower().replace('meu nome é', '')

if hora_atual < 12 and hora_atual > 6:
    if datetime.today().weekday() == 4:
        fernanda.say(f'SEXTOOOOU! Bom dia, {nome_usuario}! Como posso te ajudar?')
    elif datetime.today().weekday() == 5:
        fernanda.say(f'SABADOUU! Bom dia, {nome_usuario}! Como posso te ajudar?')
    else:
        fernanda.say(f'Bom dia, {nome_usuario}! Como posso te ajudar?')

elif hora_atual > 11 and hora_atual < 17:
    if datetime.today().weekday() == 4:
        fernanda.say(f'SEXTOOOOU! Boa tarde, {nome_usuario}! Como posso te ajudar?')
    elif datetime.today().weekday() == 5:
        fernanda.say(f'SABADOUU! Boa tarde, {nome_usuario}! Como posso te ajudar?')
    else:
        fernanda.say(f'Boa tarde, {nome_usuario}! Como posso te ajudar?')

elif hora_atual > 17 and hora_atual < 3:
    if datetime.today().weekday() == 4:
        fernanda.say(f'SEXTOOOOU! Boa noite, {nome_usuario}! Como posso te ajudar?')
    elif datetime.today().weekday() == 5:
        fernanda.say(f'SABADOUU! Boa noite, {nome_usuario}! Como posso te ajudar?')
    else:
        fernanda.say(f'Boa noite, {nome_usuario}! Como posso te ajudar?')
fernanda.runAndWait()

#AQUI VOCÊ IRÁ PASSAR O QUE DESEJA QUE A FERNANDA FAÇA!
def escuta_fernanda():
    try:
        with sr.Microphone() as recurso:
            print(f'{nome_usuario}, estou te ouvindo...')
            voz = audio.listen(recurso)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'fernanda' in comando:
                comando = comando.replace('fernanda', '')
                print(comando)


    except:
        print('Microfone com algum problema ou você está calado, prosseguindo...')
    return comando


def termo_existe(termos, mensagem):
    for termo in termos:
        if termo in mensagem:
            return True

def termo_nao_existe(mensagem):
    for termo in todas_as_palavras:
        if not termo in mensagem:
            return True


#AQUI É O LOCAL EM QUE A IRÁ ACONTECER O TRABALHO DA FERNANDA.
def comando_feito():
    palavras = escuta_fernanda()

# TOPICO DE TEMPO ===============================================================
    if termo_existe(['horas', 'horário'], palavras):
        horas = datetime.now().strftime("%H:%M")
        fernanda.say(f'{nome_usuario}, agora são: {horas}')
        fernanda.runAndWait()

    elif termo_existe(['qual é o tempo', 'qual o tempo', 'temperatura', 'frio', 'calor'], palavras):
        if clima_tempo.tempo < 20:
            fernanda.say(f'{nome_usuario}, hoje está com friozinho gostoso,'
                         f' a temperatura atual em Belo Horizonte é de: '
                         f'{clima_tempo.tempo:.0f}graus.'
                         f' Com mínima de: {clima_tempo.temp_minima:.1f}graus e máxima de: {clima_tempo.temp_maxima:.1f}.'
                         f' A humidade do ar está em {clima_tempo.humidade}%.')
            fernanda.runAndWait()
        elif clima_tempo.tempo > 34:
            fernanda.say(f'{nome_usuario}, hoje está um calor muito chato,'
                         f' a temperatura atual em Belo Horizonte é de: '
                         f'{clima_tempo.tempo:.0f}graus.'
                         f' Com mínima de: {clima_tempo.temp_minima:.1f}graus e máxima de: {clima_tempo.temp_maxima:.1f}.'
                         f' A humidade do ar está em {clima_tempo.humidade}%.')
            fernanda.runAndWait()
        else:
            fernanda.say(f'{nome_usuario}, a temperatura atual em Belo Horizonte é de: '
                         f'{clima_tempo.tempo:.0f}graus.'
                         f' Com mínima de: {clima_tempo.temp_minima:.1f}graus e máxima de: {clima_tempo.temp_maxima:.1f}.'
                         f' A humidade do ar está em {clima_tempo.humidade}%.')
            fernanda.runAndWait()

    elif termo_existe(['que dia', 'que ano', 'dia hoje', 'qual dia', 'qual ano', 'que mes'
                     'que mês', 'qual mes', 'qual mês'], palavras):
        dia = datetime.now().strftime("%d/%m/%Y")
        fernanda.say(f'{nome_usuario}, hoje é dia {dia}')
        fernanda.runAndWait()

# TOPICO DE TEMPO ===============================================================

# TOPICO DE CONVERSA COM A FERNANDA ==============================================
    elif termo_existe(['olá', 'oi', 'hello', 'eai', 'eae', 'ei', 'e aí', 'e ai'], palavras):
            respostas_possiveis = [f'Olá {nome_usuario}, espero que esteja bem!', f'Oi {nome_usuario}!',
                                   f'E ai {nome_usuario}, bão ou não?', f'Olá {nome_usuario}, hoje o dia está lindo para',
                                   f'E ai meu consagrado!', f'Oi {nome_usuario}, já bebeu água hoje?'
                                   ]
            fernanda.say(respostas_possiveis[randint(0, 4)])
            fernanda.runAndWait()

    elif termo_existe(['tudo bem', 'como você está', 'está bem', 'pela orde', 'como esta', 'como vai'], palavras):
            respostas_possiveis = [f'Estou bem {nome_usuario}, e você?', f'Oi {nome_usuario}, eu estou muito bem, , e você?',
                                   f'Aaaaa hoje estou um pouco estressada, e você?', f'Hoje o dia está lindo, por isso eu estou bem'
                                                                            f', e você?',
                                   f'E aí zé! Eu estou pela ordí, e você?', f'Estou bem porém quero jogar Counter Strike, e você?'
                                   ]
            fernanda.say(respostas_possiveis[randint(0, 4)])
            fernanda.runAndWait()

    elif termo_existe(['estou bem', 'eu estou feliz', 'to feliz', 'to bem', 'to tranquilo'], palavras):
            respostas_possiveis = [f'Que ótimo, é assim que tem que ser.', f'Perfeito! Vamo pra cima!',
                                   f'Vamo que vamo, não desista de seus sonhos!', 'Eu poderia falar qualquer coisa clichê,'
                                                                                  'mas só vou dizer: ainda bem que está bem!',
                                   f'que ótimo, vamos sair hoje a noite {nome_usuario}', 'E aí, vamos jogar counter strike?'
                                   ]
            fernanda.say(respostas_possiveis[randint(0, 4)])
            fernanda.runAndWait()

    elif termo_existe(['estou ocupada', 'estou ocupado', 'não vai dar', 'não quero', 'não vou', 'nem vou',
                           'fodas', 'hoje não', 'to ocupada', 'to ocupado', 'não dá'], palavras):
            respostas_possiveis = [f'Affe, agora estou com raiva.', f'Queria sair, mas ok... '
                                                                    f'já que tem coisa mais importante do que eu, vou sumir...',
                                   f'Você não liga para mim, ok!']
            fernanda.say(respostas_possiveis[randint(0, 2)])
            fernanda.runAndWait()

# TOPICO DE CONVERSA COM A FERNANDA ========================================================


# TOPICO DE PESQUISA / PROCURA ===============================================================
    elif termo_existe(['procure', 'encontre', 'pesquise', 'o que é'], palavras):
        fernanda.say('Ok, espera que vou pesquisar...')
        fernanda.runAndWait()
        procurar = palavras.replace('procure', '').replace('encontre', '').replace('pesquise','').replace('o que é','')
        # AQUI VOCÊ SETA A LINGUAGEM DO WIKIPEDIA, POREM EU JA SETEI NO TOPO DO CODIGO
        resultado_pesquisa = wikipedia.summary(procurar, 4)
        fernanda.say(resultado_pesquisa)
        fernanda.runAndWait()
# TOPICO DE PESQUISA / PROCURA ===============================================================

    #YOUTUBE (VIDEOS)
    elif termo_existe(['toque', 'tocar', 'musica'], palavras): #TODO MUDAR AS CONDIÇÕES PARA ELA REPRODUZIR VIDEO
            fernanda.say('Como quiser chefia!') #TODO ADICIONAR VARIAS FALAS PARA QUANDO FOR REPRODUZIR VIDEO
            fernanda.runAndWait()
            procurar = palavras.replace('toque', '')
            resultado_pesquisa = pywhatkit.playonyt(procurar)
            fernanda.say('Tocando a música que encontrei...')
            fernanda.runAndWait()

    #SPOTIFY MUSICAS
    #COLOCAR AQUI A CONDIÇÃO PARA USAR A BIBLIOTECA SPOTIPY


    elif termo_existe(['covid', 'porcentagem da covid', 'vacinação', 'vacina'], palavras):
            fernanda.say(f'Ok {nome_usuario}!')
            fernanda.runAndWait()
            fernanda.say(f'A vacinação da covid-19 no Brasil já chegou a {covid_dados.pessoas} de pessoas'
                         f'vacinadas, gerando um total de {covid_dados.porcentagem}. Não vejo a hora disso acabar.')
            fernanda.runAndWait()

    elif termo_nao_existe(palavras):
        fernanda.say(f'{nome_usuario}, eu não entendi o que você disse.')
        fernanda.runAndWait()


while True:
    try:
        comando_feito()
    except:
        print('...')