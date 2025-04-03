import flet as ft

def main(page: ft.Page):
    page.title = "Gerador de Senhas Seguras"
    instrucoes = ft.Text('No campo abaixo, insira a quantidade de caracteres que a senha deve ter:')
    qtde = ft.TextField(label='digite um valor...')
    gerar_senha = ft.ElevatedButton('Gerar senha')

    page.add(
        instrucoes, 
        qtde
    )