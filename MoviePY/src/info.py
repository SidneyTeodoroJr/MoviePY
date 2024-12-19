import flet as ft

from modules.interface_components import CustomText

def info_page():
    return ft.Column(
        [
            CustomText(value="Info Page", size=24, weight=ft.FontWeight.BOLD),
            CustomText(value="Sobre o sistema."),
        ]
    )
