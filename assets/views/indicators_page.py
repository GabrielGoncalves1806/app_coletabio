import flet as ft
from assets.models import indicators_model


def main(page: ft.Page):
    page.route = '/indicators'

    def go_home(e):
        page.views.pop()
        page.update()

    date_dropdown = indicators_model.get_collects_dates()
    chart_container = ft.Container(
        content=ft.Text('Selecione uma data acima para exibir o gráfico.'),
        padding=10,
        expand=True,
    )

    def on_date_change(e):
        selected = date_dropdown.value
        if not selected:
            return
        print(f'[indicators] data selecionada: {selected}')
        chart = indicators_model.create_chart(selected)
        if chart is None:
            chart = ft.Text(f'Sem dados para {selected}.')
        chart_container.content = chart
        page.update()

    date_dropdown.on_select = on_date_change

    page.views.append(
        ft.View(
            route='/indicators',
            controls=[
                ft.Row([
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=go_home),
                    ft.Text('Coletas', size=25),
                ]),
                date_dropdown,
                chart_container,
                ft.ElevatedButton('Voltar', on_click=go_home),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
    )
    page.update()
