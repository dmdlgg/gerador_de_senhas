import random 
import string
import flet as ft

alfabetoMins = string.ascii_lowercase
alfabetoMinsMaiusc = string.ascii_uppercase                                                               
numeros = string.digits
simbolos = string.punctuation
tudo  = [alfabetoMins, alfabetoMinsMaiusc, numeros, simbolos]

qtde = 3
senha = []

def gerar_senha(e, page, st):
    
    if int(e)<4:
        raise ValueError('A quantidade minima de caracteres sao 4!')

    while len(senha)<int(e):
        for x in tudo:
            ch = random.choice(x)
            senha.append(ch)
            if len(senha)==int(e):
                break
    random.shuffle(senha)
    senha_s = ', '.join(senha).replace(', ', '')
    st.value = f'Sua senha: {senha_s}'
    page.update()
    print('botao clicado')
