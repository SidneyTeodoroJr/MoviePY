import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

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
    
BarChart= ft.BarChart(
        max_y=100,
        expand=True,
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.WHITE24,
            dash_pattern=[3,3],
           interval=10,
            width=1

        ),

        border=ft.border.all(width=0.3, color=ft.colors.WHITE),

        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Ação"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Comédia"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text("Familia"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=4, label=ft.Container(ft.Text("Terror"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=5, label=ft.Container(ft.Text("Animação"), padding=10)
                )
            ],
            labels_size=40
        ),
        tooltip_bgcolor=ft.colors.SURFACE_VARIANT,
        bar_groups=[
            ft.BarChartGroup(
                x= 2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 40,
                        width=30,
                        color=ft.colors.RED_600,
                        border_radius=0,
                        tooltip="Comédia"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 35,
                        width=30,
                        color=ft.colors.ORANGE_300,
                        border_radius=0,
                        tooltip="Ação"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 20,
                        width=30,
                        color=ft.colors.GREEN_400,
                        border_radius=0,
                        tooltip="Família"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 4,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 57,
                        width=30,
                        color=ft.colors.PURPLE_100,
                        border_radius=0,
                        tooltip="Terror"
                    )
                ]
            ),
            ft.BarChartGroup(
                x= 5,
                bar_rods=[
                    ft.BarChartRod(
                        from_y= 0,
                        to_y= 17,
                        width=30,
                        color=ft.colors.PINK_600,
                        border_radius=0,
                        tooltip="Animação"
                    )
                ]
            )

        ]
    )