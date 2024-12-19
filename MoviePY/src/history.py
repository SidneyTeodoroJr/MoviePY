import flet as ft

from modules.interface_components import CustomText

def history_page():
    return ft.Column(
        [
            CustomText(value="History Page", size=24, weight=ft.FontWeight.BOLD),
            CustomText(value="Aqui você pode ver o histórico de filmes assistidos.")
        ]
    )
