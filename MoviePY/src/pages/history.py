import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
from modules.interface_components import CustomText, BarChart

normal_radius = 100
hover_radius = 115
normal_title_style = ft.TextStyle(
    size=20, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD
)
hover_title_style = ft.TextStyle(
    size=30,
    color=ft.Colors.WHITE,
    weight=ft.FontWeight.BOLD,
    shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK),
)

# Section data: percentages and colors
sections_data = [
    {"percentage": 40, "color": ft.Colors.RED_600},
    {"percentage": 30, "color": ft.Colors.ORANGE_300},
    {"percentage": 20, "color": ft.Colors.GREEN_400},
    {"percentage": 10, "color": ft.Colors.PURPLE_100}
]

# Hover event function
def on_chart_event(e: ft.PieChartEvent):
    for idx, section in enumerate(chart.sections):
        if idx == e.section_index:
            section.radius = hover_radius
            section.title_style = hover_title_style
        else:
            section.radius = normal_radius
            section.title_style = normal_title_style
    e.control.update()

# Generate sections dynamically
chart_sections = []
for section_data in sections_data:
    chart_sections.append(
        ft.PieChartSection(
            section_data["percentage"],
            title=f"{section_data['percentage']}%",
            title_style=normal_title_style,
            color=section_data["color"],
            radius=normal_radius,
        )
    )

# Create the pie chart
chart = ft.PieChart(
    sections=chart_sections,
    sections_space=5,
    center_space_radius=50,
    on_chart_event=on_chart_event,
    expand=True,
)

# Function that returns the page with the graph
def history_page():
    return ft.Column(
        [
            CustomText(value="History Acesse", size=24, weight=ft.FontWeight.BOLD),
            CustomText(value="Here you can see the history of your most watched content.", color=ft.Colors.GREY_500),

            BarChart,
            chart,

            CustomText(value="All data is kept stored locally", size=24, weight=ft.FontWeight.BOLD),
            CustomText(value="This APP stores data locally, offering greater speed. In addition, it reduces server costs and data traffic.", color=ft.Colors.GREY_500)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30
    )