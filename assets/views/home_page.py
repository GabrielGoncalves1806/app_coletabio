import flet as ft
from assets.models import plants_model
from assets.views import collect_page, plants_page, reports_page, indicators_page
from assets.widgets import widgets

# Função que renderiza a tela Home
def main(page:ft.Page):
    page.route = '/'
    # Definiçãoes da pagina
    page.window_width = 500
    page.window_height = 650
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Coleta BIO"
    #page.window_full_screen = True
    
    navigation_bar_widget = widgets.navigation_bar()
    app_bar_widget = widgets.app_bar()
    

    def route_change(e):
        print(page.route)
        set_save_button()

    def go_to(e):
        if e.control.selected_index == 0:
            collect_page.main(page)
        
        elif e.control.selected_index == 1:
            reports_page.main(page)
        
        elif e.control.selected_index == 2:
            indicators_page.main(page)
            
        elif e.control.selected_index == 3:
            plants_page.main(page)
        

        

    def save_collect():
        page.snack_bar = ft.SnackBar(content=ft.Text(""))
        try:
            response = plants_model.save_data_on_cloud()
            print(response)
            if response == True:
                page.snack_bar.content = ft.Text('Coleta salva com sucesso!')
                page.snack_bar.open = True
                page.update()
            else:
                page.snack_bar.content = ft.Text(f'Erro ao salvar coleta - status {response}')
                page.snack_bar.open = True
                page.update()
        except Exception as e:
            pass
        set_save_button()

    save_button = ft.ElevatedButton('Save on cloud',icon='cloud_upload',on_click=lambda _: save_collect())

    def set_save_button():
        disable = plants_model.verify_temporary_data()
        if disable:
            save_button.disabled = False
            page.update()
        else:
            save_button.disabled = True
            page.update()

    set_save_button()

    
    
    # Criação da View que terá os widgets da janela
    
    page.views.append(ft.View(
            route='/',
            controls=[
                ft.Image('logo.png',width=150,height=150, border_radius=25),
                ft.Text('Projeto Coleta BIO',size=25, font_family='bold'),
                # ft.ElevatedButton('Coleta', on_click= lambda _: collect_page.main(page)),
                # ft.ElevatedButton('Relatórios', on_click= lambda _: reports_page.main(page)),
                # ft.ElevatedButton('Indicadores', on_click=lambda _: indicators_page.main(page)),
                # ft.ElevatedButton('Plantas', on_click= lambda _: plants_page.main(page)),
                save_button,
                #ft.IconButton(icon=ft.icons.REFRESH, on_click=lambda _: set_save_button()),
                #ft.ElevatedButton('Sair', bgcolor=ft.colors.RED,on_click= lambda _: page.window_close())
            ],
            navigation_bar=navigation_bar_widget,
            appbar=app_bar_widget,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            vertical_alignment= ft.MainAxisAlignment.CENTER
        )
    )
    
    print(navigation_bar_widget.selected_index)
    navigation_bar_widget.on_change = go_to
    page.on_route_change = route_change

    page.update()
   