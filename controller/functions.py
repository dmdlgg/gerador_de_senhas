import random 
import string
 
alfabetoMins = string.ascii_lowercase
alfabetoMinsMaiusc = string.ascii_uppercase                                                               
numeros = string.digits
simbolos = string.punctuation
tudo  = [alfabetoMins, alfabetoMinsMaiusc, numeros, simbolos]

qtde = 8
senha = []

while len(senha)<qtde:
    for x in tudo:
        ch = random.choice(x)
        senha.append(ch)
        if len(senha)==qtde:
            break
random.shuffle(senha)
senha_s = ', '.join(senha).replace(', ', '')
print(senha_s)