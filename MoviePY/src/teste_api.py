import flet as ft
import requests

# Sua chave de API da TMDb
API_KEY = "845b28103013450036863c5c2a958bf9"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

def fetch_movies():
    """Obtém filmes populares da API TMDb."""
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": API_KEY, "language": "pt-BR", "page": 1}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Erro ao obter filmes:", response.status_code, response.text)
        return []

def main(page: ft.Page):
    page.title = "Recomendador de Filmes 🎥"
    page.scroll = "auto"
    page.padding = 10
    
    def load_movies():
        """Carrega filmes populares na interface."""
        movies = fetch_movies()
        if not movies:
            page.add(ft.Text("Erro ao carregar filmes. Tente novamente mais tarde.", color="red"))
        else:
            for movie in movies:
                poster_url = IMAGE_BASE_URL + movie["poster_path"] if movie.get("poster_path") else ""
                page.add(
                    ft.Card(
                        content=ft.Column([
                            ft.Row([
                                ft.Image(src=poster_url, 
                                        height=500, 
                                        width=450, 
                                        fit = ft.ImageFit.CONTAIN,
                                        repeat = ft.ImageRepeat.NO_REPEAT,
                                        filter_quality= ft.FilterQuality.LOW,
                                        border_radius = ft.border_radius.all(10)
                                ),

                                ft.Column([
                                    ft.Text(movie["title"], size=20, weight="bold", selectable=True),
                                    ft.Text(f"Nota: {movie['vote_average']}", color="green", selectable=True),
                                    ft.Text(movie["overview"], max_lines=3, overflow="ellipsis", selectable=True),
                                ], spacing=10)
                            ], spacing=10),
                        ], spacing=10),
                        margin=ft.margin.only(bottom=10),
                    )
                )
        page.update()

    # Título da aplicação
    page.add(ft.Text("Filmes Populares", size=24, weight="bold"))
    
    # Botão para carregar os filmes
    page.add(
        ft.ElevatedButton(
            text="Carregar Filmes",
            on_click=lambda _: load_movies(),
            color="white",
            bgcolor="blue"
        )
    )

ft.app(target=main)