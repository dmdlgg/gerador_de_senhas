import random 
import string
import flet as ft

alfabetoMins = string.ascii_lowercase
alfabetoMinsMaiusc = string.ascii_uppercase                                                               
numeros = string.digits
simbolos = '@#$%&*!'
tudo  = [alfabetoMins, alfabetoMinsMaiusc, numeros, simbolos]

def gerar_senha(e, page, st, erro):

    senha = []
    
    try:
        qtde = int(e)
        if qtde<4:
            erro.value = f'sua senha deve ter mais de 4 caracteres!'
            page.update()
            return

        for grupo in tudo:
            senha.append(random.choice(grupo)) 
        while len(senha)<qtde:
            for x in tudo:
                ch = random.choice(x)
                senha.append(ch)
                if len(senha)==qtde:
                        break
        random.shuffle(senha)
        senha_s = ', '.join(senha).replace(', ', '')
        erro.value = ""
        st.value = f'Sua senha: {senha_s}'
        page.update()

    except ValueError:
        st.value = f''
        erro.value = f'insira um número!'
        page.update()