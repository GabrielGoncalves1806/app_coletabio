import flet as ft
from assets.models import indicators_model

def main(page:ft.Page):

    
    collect_dates = indicators_model.get_collects_dates()
    graphic = ft.BarChart()
    page.route = '/indicators'
    
    def go_home(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    def collect_date_chart(dp_date):
        indicators.controls.pop(1)
        graphic = indicators_model.create_chart(dp_date)
        indicators.controls.insert(1,graphic)
        page.update()

    indicators = ft.View(
            route='/indicators',
            controls=[
                # Header
                ft.Column(
                    [
                        ft.Row([ft.Text('')]),
                        ft.Row([ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_home),ft.Text(f'Coletas',size=25)]),
                        collect_dates,
                        ft.Row([ft.Text(' ')])
                    ],
                ),
                # Body
                ft.Column(
                    [

                    ],
                    
                ),

                # Footer
                ft.Column(
                    [
                        ft.ElevatedButton('Voltar',on_click=go_home)
                    ]
                )
            ]
        )
    page.views.append(indicators)
    collect_dates.on_change = lambda _: collect_date_chart(collect_dates.value)
    page.update()