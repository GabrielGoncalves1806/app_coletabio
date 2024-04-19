import flet as ft
from assets.models import reports_model

def main(page: ft.Page):
    page.route = '/reports'
    page.scroll = True

    def go_home(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def sort(e):
        page_body.controls.reverse()
        page.update()
    
    page_body, reports_count = reports_model.get_reports_list()

    page.views.append(
        ft.View(route='/plants',
            controls=[
                # Header
                ft.Column(
                    [
                        ft.Row([ft.Text('')]),
                        ft.Row([ft.IconButton(ft.icons.ARROW_BACK,on_click=go_home),ft.Text('Relatórios',font_family='Bold',size=25)]),
                        ft.Row([ft.Text(f'Encontrados: {reports_count}'),ft.IconButton(ft.icons.SORT,on_click=sort)])
                    ]
                ),
                # Body
                ft.Column(
                    [
                        page_body,
                    ],
                    scroll=True
                ),
                # Footer
                ft.Column(
                    [
                        ft.ElevatedButton('Voltar', on_click=go_home)
                    ]
                ),
            ],
            scroll=True
        )
    )
    #show_reports()
    
    page.update()