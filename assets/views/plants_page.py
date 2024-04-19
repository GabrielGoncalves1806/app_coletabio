import flet as ft
from assets.models import plants_model

def main(page: ft.Page):
    page.route = '/plants'
    page_body = ft.Column()
    

    def show_plants():
        plants = plants_model.get_plants_info()
        for plant in plants:
            page_body.controls.append(  
                    ft.Column(
                        [
                            ft.Text(plant,size=25),
                            ft.Image(src=f'assets/{plants[plant]['file']}'),
                            ft.Text(str(plants[plant]['info']).encode('utf-8').decode('utf-8'),selectable=True)
                        ],
                        alignment=ft.alignment.center,
                    ),
                )
            
    def go_home(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.views.append(
        ft.View(route='/plants',
                controls=[
                    # Header
                    ft.Column(
                        [
                            ft.Row([ft.Text('')]),
                            ft.Row([ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_home),ft.Text("Plantas Observadas",size=25)])
                        ],
                    ),
                    # Body
                    ft.Column(
                        [
                            page_body, 
                        ]
                    ),
                    # Footer
                    ft.Column(
                        [
                            ft.ElevatedButton('Voltar', on_click=go_home)
                        ]
                    )
                    # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    # alignment=ft.MainAxisAlignment.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                scroll=True
            )
    )
    show_plants()
    
    
    page.update()

