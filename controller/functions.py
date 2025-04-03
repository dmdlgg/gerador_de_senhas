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

def gerar_senha(e, page, st, erro):
    try:
        if int(e)<4:
            erro.value = f'sua senha deve ter mais de 4 caracteres!'
            page.update()

        else:   
            while len(senha)<int(e):
                for x in tudo:
                    ch = random.choice(x)
                    senha.append(ch)
                    if len(senha)==int(e):
                        break
            random.shuffle(senha)
            senha_s = ', '.join(senha).replace(', ', '')
            erro.value = ""
            st.value = f'Sua senha: {senha_s}'
            page.update()
            print('botao clicado')
    except ValueError:
        erro.value = f'insira um número!'
        page.update()