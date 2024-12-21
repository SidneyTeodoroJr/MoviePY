import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
from modules.interface_components import *  

from pages.welcome import welcome_page
from pages.history import history_page  
from pages.list import list_page
from pages.info import info_page

def main(page: ft.Page) -> None:
    page.title = "MoviesPY"
    page.theme_mode = ft.ThemeMode.DARK

    # Scrollbar
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(thumb_color=ft.Colors.with_opacity(0.3, 'white'))
    )

    # Controls the selected index of the NavigationBar
    selected_index = 0

    def navigate_to_page(index: int):
        """Função para navegação baseada na seleção do NavigationBar"""
        nonlocal selected_index
        selected_index = index  # Atualiza o índice selecionado
        if index == 0:
            page.go("/home")
        elif index == 1:
            page.go("/history")
        elif index == 2:
            page.go("/list")
        elif index == 3:
            page.go("/info")

    def route_change(e) -> None:
        """Function called when route changes"""
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        welcome_page(page)
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        elif page.route == "/home":
            def releases_click(e):
                print("releases")

            def films_click(e):
                print("films")

            def series_click(e):
                print("series")

            def tendencies_click(e):
                print("tendencies")

            def child_family_click(e):
                print("child_family")

            releases = MovieCard(
                src="https://image.tmdb.org/t/p/w600_and_h900_bestv2/cWsd33Nwp3tgYB5LMMadl3qVMKh.jpg",
                scroll="AUTO",
                width=300,
                height=450,
                icon_size=30,
                on_click=releases_click,
            ).build(count=5)

            films = MovieCard(
                src="https://image.tmdb.org/t/p/w600_and_h900_bestv2/pnXLFioDeftqjlCVlRmXvIdMsdP.jpg",
                scroll="AUTO",
                width=150,
                height=225,
                icon_size=20,
                on_click=films_click,
            ).build(count=25)

            series = MovieCard(
                src="https://image.tmdb.org/t/p/w600_and_h900_bestv2/kGRWWvRpI2SVDYnvM3gJb21X0QL.jpg",
                scroll="AUTO",
                width=150,
                height=225,
                icon_size=20,
                on_click=series_click,
            ).build(count=25)

            tendencies = MovieCard(
                src="https://image.tmdb.org/t/p/w600_and_h900_bestv2/gyDVzU2A8bdK4fsS4rWTsDcPPEB.jpg",
                scroll="AUTO",
                width=150,
                height=225,
                icon_size=20,
                on_click=tendencies_click,
            ).build(count=25)

            child_family = MovieCard(
                src="https://image.tmdb.org/t/p/w600_and_h900_bestv2/8HzA55GCjRTEC2YhPGna8Lc8qHo.jpg",
                scroll="AUTO",
                width=150,
                height=225,
                icon_size=20,
                on_click=child_family_click,
            ).build(count=25)

            Everyone_likes = MovieCard(
                src="https://image.tmdb.org/t/p/w600_and_h900_bestv2/6AtoMpHvs9pxd30KsyK8QmJ9W9M.jpg",
                scroll="AUTO",
                width=150,
                height=225,
                icon_size=20,
                on_click=child_family_click,
            ).build(count=10)

            ft.floating_action_button = ft.FloatingActionButton(
                icon=ft.Icons.SEARCH,
                bgcolor=ft.Colors.BLACK,
                opacity=0.8,
                foreground_color=ft.Colors.WHITE,
                highlight_elevation=16,
                shape=ft.RoundedRectangleBorder(radius=30),
                tooltip="ADD",
                on_click=lambda e: print("SEARCH clicked!"),
            )

            nav_bar = create_navbar(navigate_to_page, selected_index)

            page.views.append(
                ft.View(
                    route="/home",
                    controls=[
                        APPBar,
                        ft.floating_action_button,
                        nav_bar,
                        releases,
                        CustomText(value="Most viewed Films"),
                        films,
                        CustomText("Featured series"),
                        series,
                        CustomText(value="Tendencies"),
                        tendencies,
                        CustomText(value="Child & family for you"),
                        child_family,
                        CustomText(value="Everyone likes"),
                        Everyone_likes,
                    ],
                    scroll="AUTO",
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        elif page.route == "/history":
            nav_bar = create_navbar(navigate_to_page, selected_index)
            
            page.views.append(
                ft.View(
                    route="/history",
                    controls=[
                        APPBar,
                        history_page(),
                        nav_bar,
                    ],
                    scroll="AUTO",
                )
            )

        elif page.route == "/list":
            nav_bar = create_navbar(navigate_to_page, selected_index)
            page.views.append(
                ft.View(
                    route="/list",
                    controls=[
                        APPBar,
                        list_page(),
                        nav_bar,
                    ],
                    scroll="AUTO",
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        elif page.route == "/info":
            nav_bar = create_navbar(navigate_to_page, selected_index)
            page.views.append(
                ft.View(
                    route="/info",
                    controls=[
                        APPBar,
                        info_page(),
                        nav_bar,
                    ],
                    scroll="AUTO",
                )
            )

        page.update()

    def view_pop(e, ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER, web_renderer=ft.WebRenderer.HTML)