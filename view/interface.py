import flet as ft
from controller.functions import gerar_senha

def main(page: ft.Page):
    page.title = "Gerador de Senhas Seguras"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    instrucoes = ft.Text(
        'No campo abaixo, insira a quantidade de caracteres que a senha deve ter:',
        text_align="center"
    )

    qtde = ft.TextField(
        label='digite um valor...',
        width=200,
        text_align="center"
    )

    senha_texto = ft.Text("", text_align="center")
    erro = ft.Text("", text_align="center")

    gerar = ft.ElevatedButton(
        'Gerar senha', 
        on_click=lambda e: gerar_senha(qtde.value, page, senha_texto, erro)
    )

    page.add(
        ft.Column(
            [
                instrucoes, 
                qtde,
                gerar,
                senha_texto,
                erro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )