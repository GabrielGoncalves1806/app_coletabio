import flet as ft
from assets.models import plants_model

# Função que renderiza a janela de coleta
def main(page:ft.Page):
    page.route = '/collect'
    # Definições da pagina
    page.scroll = True

    # Variavel que vai conter o corpo(page_body) da janela
    page_body = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # Função que cria os formularios
    def create_form():

        # Cria uma variavel que recebe o json que contem os nomes das especies
        plants = plants_model.get_plants_from_data()
        
        # Adiciona no page_body(corpo) um formulario para cada especie no json
        for plant in plants:
            page_body.controls.append(
                ft.Column(
                    [
                        ft.Text(value=str(plant)),
                        ft.TextField(label='Volume coletado',autofocus=True,suffix_text='ml',keyboard_type='NUMBER')
                    ]
                )
            ),
    
    # Função que retorna para a tela Home
    def go_home(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        page.update()

    # Função que acessa o model plants_model e chama a função que salva o json local na nuvem
    def save_data(e):
        plants_model.save_temporary_data(page_body)
        # Após salvar volta pra home
        go_home(e)

    # Criação da View que terá os widgets da janela
    page.views.append(
        ft.View(
            route='/collect',
            scroll= True,
            controls=[

                # Header
                ft.Column(
                    [
                        ft.Row([ft.Text('')]),
                        ft.Row([ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_home),ft.Text("Coleta de Dados",size=25)])
                    ]
                ),

                # Body
                ft.Column(
                    [
                        page_body,
                    ]
                ),
                
                # Footer
                ft.Column([
                    ft.Row([
                        ft.ElevatedButton('Voltar',on_click=go_home),
                        ft.ElevatedButton('Salvar', on_click=save_data)
                    ])
                ])
            ]
        )
    )

    # Chama a criação dos formularios para depois atualizar a janela
    create_form()
    
    page.update()