import flet as ft
import random
from modules.interface_components import CustomText

def welcome_page(page):
    gif = [
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmx6dXY3cW5kZDVraGM4eWR3M2h2MmZ4NnhqcHdvNzd0amJuemV1eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3osxYzXXuBSzXZ1Np6/giphy.webp",
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnptcm9vcjE1bWx6YWpoN3hlenRhNnd6cXRjcmNhcnNkZGVzaXF4ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3rgXBsoArl2iTjcXni/giphy.webp",
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWoxeTI4amp3bzh0NDlwOXBpcDkyaWJjcm8yc2JieHljazQzMG5hZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PCFK39ruKPdnc4Km4h/giphy.webp",
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnh3NWFseGR1MmtsZ2s1ODRlem1xYzZ5N3JuejRyZmM4NjM5d2lhdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZeiZdsBk9KCBK9PJ7r/giphy.webp",
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExemVlcWNiMXdza2o2MWxmMGd3bHAybTRwaGs0czB0ZjJsam0xNWVzeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SqejLXBygoLmM/giphy.webp",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTV6aTlxMTIxMXgyMnp3Nm1sd3lhOXkyenpmcWg2YTJrMTUxcTc3biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tBpYqkMgAPaWA/giphy.webp"
    ]
    
    # Escolher uma imagem aleatória da lista
    random_image = random.choice(gif)
    
    return ft.Stack(
        [
            # Exibir a imagem aleatória
            ft.Image(
                src=random_image,
                repeat=ft.ImageRepeat.NO_REPEAT,
                fit=ft.ImageFit.CONTAIN,
                
                width=500,
                height=500,
            ),
            
            # Outros componentes (Texto e Botão)
            ft.Column(
                [
                    CustomText(value="Welcome to MoviesPY!", size=35),
                    CustomText(value="The fun doesn't end here."),
                    ft.ElevatedButton(
                        "Go to APP",
                        icon=ft.Icons.LOCAL_MOVIES_SHARP,
                        color="black",
                        bgcolor="white",
                        on_click=lambda e: page.go("/home"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        width=500,
        height=500,
    )