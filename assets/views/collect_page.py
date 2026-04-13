import flet as ft
from assets.models import plants_model


def main(page: ft.Page):
    page.route = '/collect'

    form_fields = []
    body_controls = []

    plants = plants_model.get_plants_from_data()
    for plant in plants:
        field = ft.TextField(
            label='Volume coletado',
            suffix=ft.Text('ml'),
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        form_fields.append((str(plant), field))
        body_controls.append(
            ft.Column([ft.Text(str(plant)), field])
        )

    def go_home(e):
        page.views.pop()
        page.update()

    def save_data(e):
        fake_body = ft.Column(
            controls=[ft.Column([ft.Text(name), field]) for name, field in form_fields]
        )
        plants_model.save_temporary_data(fake_body)
        go_home(e)

    controls = [
        ft.Row([
            ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=go_home),
            ft.Text("Coleta de Dados", size=25),
        ]),
        *body_controls,
        ft.Row([
            ft.ElevatedButton('Voltar', on_click=go_home),
            ft.ElevatedButton('Salvar', on_click=save_data),
        ]),
    ]

    page.views.append(
        ft.View(
            route='/collect',
            controls=controls,
            scroll=ft.ScrollMode.AUTO,
        )
    )
    page.update()
