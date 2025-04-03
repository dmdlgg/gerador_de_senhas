import flet as ft
from controller.functions import gerar_senha

def main(page: ft.Page):
    page.title = "Gerador de Senhas Seguras"
    instrucoes = ft.Text('No campo abaixo, insira a quantidade de caracteres que a senha deve ter:')
    qtde = ft.TextField(label='digite um valor...')
    senha_texto = ft.Text("")
    gerar = ft.ElevatedButton('Gerar senha', on_click=lambda e: gerar_senha(qtde.value, page, senha_texto))
    

    page.add(
        instrucoes, 
        qtde,
        gerar,
        senha_texto
        
    )