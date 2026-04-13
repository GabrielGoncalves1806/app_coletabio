import flet as ft
from assets.models import plants_model


def main(page: ft.Page):
    page.route = '/plants'

    def go_home(e):
        page.views.pop()
        page.update()

    controls = [
        ft.Row([
            ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=go_home),
            ft.Text("Plantas Observadas", size=25),
        ]),
    ]

    plants = plants_model.get_plants_info()
    for name, info in plants.items():
        controls.append(
            ft.Column(
                [
                    ft.Text(name, size=22, weight=ft.FontWeight.BOLD),
                    ft.Image(src=info['file'], fit=ft.BoxFit.CONTAIN, width=280),
                    ft.Text(info['info'], selectable=True),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    controls.append(ft.ElevatedButton('Voltar', on_click=go_home))

    page.views.append(
        ft.View(
            route='/plants',
            controls=controls,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        )
    )
    page.update()
