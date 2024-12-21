import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
from modules.interface_components import CustomText

def info_page():
    return ft.Column(
        [
            ft.Image(
                src=f"https://avatars.githubusercontent.com/u/91035485?s=400&u=67a9a286015cdfbdf8fab3865c30e468113b208c&v=4",
                width=150,
                height=150,
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(100),
            ),
            CustomText(value="Autor: Sidney T. A. Junior"),

            CustomText(value="Contact:"),

            CustomText(value="+55 (27) 99648-9123", color=ft.Colors.GREY_500, size=16),
            CustomText(value="sidneyteodoro2002@gmail.com", color=ft.Colors.GREY_500, size=16),
            CustomText(value="@sidney_teodoro_araujo", color=ft.Colors.GREY_500, size=16),

            CustomText(value="Importante", color=ft.Colors.RED_500),

            CustomText(value="""This APP is for educational and demonstration purposes. The main goal of this app is to demonstrate the potential of Python and the Flat library in developing cross-platform applications! Flet is a framework that allows the creation of web, desktop and mobile applications in Python, even for those without frontend development experience. It uses controls inspired by Google's Flutter, but goes further by integrating smaller widgets and simplifying complexities. Flet adopts UI best practices and sensible patterns, ensuring that the resulting applications look elegant and polished, without requiring much design effort."""
                       ,color=ft.Colors.GREY_500, size=15),

            CustomText(value="Version: 0.1.0 (2024)", color=ft.Colors.GREY_500, size=15)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30
    )