import flet as ft

APPBar = ft.AppBar(
    title=ft.Text("MoviesPY", weight=ft.FontWeight.BOLD),
    center_title=True,
    bgcolor=ft.Colors.TRANSPARENT,
    automatically_imply_leading=False,
)

def create_navbar(navigate_to_page, selected_index):
    return ft.NavigationBar(
        selected_index=selected_index,  # Passa o índice selecionado
        on_change=lambda e: navigate_to_page(e.control.selected_index),  # Passa o índice da navegação
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME_ROUNDED,
                label="Home"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.HISTORY,
                selected_icon=ft.Icons.HISTORY_TOGGLE_OFF_OUTLINED,
                label="History"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="My list",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.INFO_OUTLINED,
                selected_icon=ft.Icons.INFO_ROUNDED,
                label="Info",
            )
        ]
    )

class MovieCard:
    def __init__(self, src: str, scroll: str, width: int, height: int, icon_size: int, on_click):
        self.src = src
        self.scroll = scroll
        self.width = width
        self.height = height
        self.icon_size = icon_size
        self.on_click = on_click

    def build(self, count: int):
        return ft.Row(
            expand=False,
            wrap=False,
            scroll=self.scroll,
            controls=[
                ft.Container(
                    image_src=self.src,
                    content=ft.Column([
                        ft.IconButton(
                            icon=ft.Icons.BOOKMARK_BORDER,
                            icon_color="white",
                            icon_size=self.icon_size,
                            tooltip="Save",
                        )
                    ], alignment=ft.MainAxisAlignment.END),
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    alignment=ft.alignment.center,
                    width=self.width,  # Largura
                    height=self.height,  # Altura
                    ink=True,
                    on_click=self.on_click,
                ) for _ in range(count)
            ]
        )

class AttendingRow:
    def __init__(self, image_src: str, title: str, icon_size: int = 40, on_click=None):
        self.image_src = image_src
        self.title = title
        self.icon_size = icon_size
        self.on_click = on_click if on_click else lambda e: print("Play")

    def build(self):
        return ft.Stack(
            controls=[
                ft.Image(
                    src=self.image_src,
                    fit=ft.ImageFit.CONTAIN,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=5,
                    filter_quality=ft.FilterQuality.LOW,
                ),
                ft.Column(
                    controls=[
                        ft.Text(self.title, 
                            size=25,
                            weight=ft.FontWeight.BOLD,
                            no_wrap=False
                        ),
                        ft.IconButton(
                            icon=ft.Icons.PLAY_CIRCLE,
                            icon_color=ft.colors.WHITE,
                            icon_size=self.icon_size,
                            tooltip="Play",
                            on_click=self.on_click
                        ),
                    ], 
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
            ],
            height=200,
            width=300,
        )

class Attending:
    def __init__(self, image_sources: list, titles: list):
        self.image_sources = image_sources
        self.titles = titles

    def build(self):
        return ft.Row(
            expand=False,
            wrap=False,
            scroll="AUTO",
            controls=[
                AttendingRow(image_src=self.image_sources[i], title=self.titles[i]).build()
                for i in range(len(self.image_sources))
            ]
        )

class CustomText(ft.Text):
    def __init__(self, value=str, color=ft.Colors.WHITE, size: int=20, weight: ft.FontWeight = ft.FontWeight.W_300, selectable=True):
        super().__init__()

        self.value=value
        self.color=color
        self.size=size
        self.weight=weight
        self.selectable=selectable

    def build(self):
        return ft.Text(
            value=self.value,
            color=self.color,
            size=self.size,
            weight=self.weight,
            selectable=self.selectable
        )