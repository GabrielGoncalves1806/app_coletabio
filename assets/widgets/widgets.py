import flet as ft

def navigation_bar():
    navigation_bar = ft.CupertinoNavigationBar(
        destinations=[
            #ft.NavigationDestination(label='Inicio',icon='HOME'),
            ft.NavigationDestination(label='Coleta',icon='ADD'),
            ft.NavigationDestination(label='Relatórios',icon='FORMAT_LIST_BULLETED'),
            ft.NavigationDestination(label='Indicadores',icon='BAR_CHART'),
            ft.NavigationDestination(label='Especies',icon='FOREST_OUTLINED',selected_icon='FOREST')
        ],
    )
    
    return navigation_bar

def app_bar():
    app_bar = ft.AppBar(
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text='Configurações',icon=ft.icons.SETTINGS_OUTLINED)
                ],
            )
        ]
    )
    return app_bar