import flet as ft

def navigation_bar():
    navigation_bar = ft.CupertinoNavigationBar(
        destinations=[
            ft.NavigationBarDestination(label='Coleta', icon=ft.Icons.ADD),
            ft.NavigationBarDestination(label='Relatórios', icon=ft.Icons.FORMAT_LIST_BULLETED),
            ft.NavigationBarDestination(label='Indicadores', icon=ft.Icons.BAR_CHART),
            ft.NavigationBarDestination(label='Especies', icon=ft.Icons.FOREST_OUTLINED, selected_icon=ft.Icons.FOREST),
        ],
    )

    return navigation_bar

def app_bar():
    app_bar = ft.AppBar(
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(content=ft.Text('Configurações')),
                ],
            )
        ]
    )
    return app_bar