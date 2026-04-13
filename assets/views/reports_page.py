import flet as ft
from assets.models import reports_model


def main(page: ft.Page):
    page.route = '/reports'

    def go_home(e):
        page.views.pop()
        page.update()

    body_column, reports_count = reports_model.get_reports_list()

    def sort(e):
        if isinstance(body_column, ft.Column):
            body_column.controls.reverse()
            page.update()

    page.views.append(
        ft.View(
            route='/reports',
            controls=[
                ft.Row([
                    ft.IconButton(ft.Icons.ARROW_BACK, on_click=go_home),
                    ft.Text('Relatórios', size=25, weight=ft.FontWeight.BOLD),
                ]),
                ft.Row([
                    ft.Text(f'Encontrados: {reports_count}'),
                    ft.IconButton(ft.Icons.SORT, on_click=sort),
                ]),
                ft.Container(content=body_column, expand=True),
                ft.ElevatedButton('Voltar', on_click=go_home),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
    )
    page.update()
