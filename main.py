import flet as ft
from assets.views import home_page

# Chama o app home que renderiza a primeira tela
ft.app(home_page.main, assets_dir='/assets')
