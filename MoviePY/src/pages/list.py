import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
from modules.interface_components import CustomText

class CustomCupertinoListTile(ft.UserControl):
    def __init__(self, 
                 title: str, 
                 subtitle: str, 
                 image_url: str, 
                 on_delete: callable = None, 
                 on_click: callable = None):
        super().__init__()
        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url
        self.on_delete = on_delete
        self.on_click = on_click

    def build(self):
        return ft.CupertinoListTile(
            bgcolor=ft.Colors.BLACK,
            leading=ft.Image(
                src=self.image_url,
            ),
            leading_size=100,
            title=CustomText(value=self.title),
            subtitle=CustomText(value=self.subtitle, size=15, color=ft.Colors.GREY_500),
            trailing=ft.IconButton(
                icon=ft.Icons.DELETE,
                icon_color=ft.Colors.RED_900,
                on_click=self.on_delete
            ),
            on_click=self.on_click,
        )


def list_page():
    def delete_action(e):
        print("Delete movie list")

    def play_action(e):
        print("Play to movie list")

    items = [
        {
            "title": "Wonder Woman: Bloodlines",
            "subtitle": "Everyone deserves the chance to fly.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/3p4lA8bzyUZvjHcI1qWmasgbEo8.jpg"
        },
        {
            "title": "The Lion King",
            "subtitle": "The circle of life has never been so exciting.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/2q22B1pewjsMIkCGxtCpl8bhs0D.jpg"
        },
        {
            "title": "Avengers: Endgame",
            "subtitle": "The fate of the universe hangs in the balance.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/7jvlqGsxeMKscskuUZgKk0Kuv99.jpg"
        },
        {
            "title": "Interstellar",
            "subtitle": "A Journey to Save the Future.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/nCbkOyOMTEwlEV0LtCOvCnwEONA.jpg"
        },
        {
            "title": "Matrix Resurrections",
            "subtitle": "The future will be rewritten.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/9DT4WVqZqBEI9Kub18gZ3m1D89m.jpg"
        },
        {
            "title": "Terminator 2: Judgment Day",
            "subtitle": "The battle to save the future begins now.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/nb0ertLALhkUqpmcahDFplqyc0I.jpg"
        },
        {
            "title": "Inception",
            "subtitle": "One idea can change the destiny of the world.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/k3UoZhRHg6h2XYzwNAJJvGC2yev.jpg"
        },
        {
            "title": "The Lord of the Rings: The Fellowship of the Ring",
            "subtitle": "The adventure begins to save Middle-earth.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/omoMXT3Z7XrQwRZ2OGJGNWbdeEl.jpg"
        },
        {
            "title": "Black Panther",
            "subtitle": "The legacy of a hero that cannot be forgotten.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/ubXNpxL2ASSzY0f8Hxv08pOsV2L.jpg"
        },
        {
            "title": "Guardians of the Galaxy",
            "subtitle": "The galaxy has never been more at risk.",
            "image_url": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/xaY92XMToaSnBuvCui3LHzNGqZB.jpg"
        }
    ]


    # Render the list items
    list_tiles = [
        CustomCupertinoListTile(
            title=item["title"],
            subtitle=item["subtitle"],
            image_url=item["image_url"],
            on_delete=delete_action,
            on_click=play_action,
        ) for item in items
    ]

    return ft.Column(
        list_tiles,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30,
    )
