import flet as ft

from modules.interface_components import CustomText

def list_page():
    return ft.Column(
        [
            CustomText(value="My List Page", size=24, weight=ft.FontWeight.BOLD),
            CustomText(value="Aqui você pode ver a minha lista pessoal"),
        ]
    )
