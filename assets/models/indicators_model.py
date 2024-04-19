import flet as ft
from assets.models import fb_model
#import fb_model


def get_collects_dates():
    collect_dates = []
    dp_with_dates = ft.Dropdown(label="Selecione a data da coleta")
    
    try:
        data_info = fb_model.get_cloud_data()
        for info in reversed(data_info['coletas']):
            for date in data_info['coletas'][info]:
                collect_dates.append(date)
                dp_with_dates.options.append(ft.dropdown.Option(str(date)))
        return dp_with_dates
    except Exception as e:
        return dp_with_dates

get_collects_dates()

def create_chart(date_of_collect):
    aroeiras = []
    angicos = []
    juremas = []
    marmeleiros = []
    externas = []
    try:
        data_info = fb_model.get_cloud_data()
        for info in data_info['coletas']:
            for date in data_info['coletas'][info]:
                if date == date_of_collect:
                    for collect in data_info['coletas'][info][date]:
                        if collect in ['Aroeira 1', 'Aroeira 2', 'Aroeira 3']:
                            aroeiras.append(float(data_info['coletas'][info][date][collect]))
                        elif collect in ['Angico 1','Angico 2','Angico 3']:
                            angicos.append(float(data_info['coletas'][info][date][collect]))
                        elif collect in ['Jurema 1','Jurema 2','Jurema 3']:
                            juremas.append(float(data_info['coletas'][info][date][collect]))
                        elif collect in ['Marmeleiro 1','Marmeleiro 2','Marmeleiro 3']:
                            marmeleiros.append(float(data_info['coletas'][info][date][collect]))
                        elif collect in ['Externa 1','Externa 2','Externa 3']:
                            externas.append(float(data_info['coletas'][info][date][collect]))
                    break

        average = [
            sum(aroeiras)/len(aroeiras),
            sum(angicos)/len(angicos),
            sum(juremas)/len(juremas),
            sum(marmeleiros)/len(marmeleiros),
            sum(externas)/len(externas)
            ]
        
        chart = ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            width=40,
                            tooltip=round(sum(aroeiras)/len(aroeiras),2),
                            from_y=0,
                            to_y=sum(aroeiras)/len(aroeiras),
                            color='#B2E2F2',
                            border_radius=0
                        ),
                    ]
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[
                        ft.BarChartRod(
                            width=40,
                            tooltip=round(sum(angicos)/len(angicos),2),
                            from_y=0,
                            to_y=sum(angicos)/len(angicos),
                            color='#B0C2F2',
                            border_radius=0
                        ),
                    ]
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[
                        ft.BarChartRod(
                            width=40,
                            tooltip=round(sum(juremas)/len(juremas),2),
                            from_y=0,
                            to_y=sum(juremas)/len(juremas),
                            color='#CAACF9',
                            border_radius=0
                        ),
                    ]
                ),
                ft.BarChartGroup(
                    x=3,
                    bar_rods=[
                        ft.BarChartRod(
                            width=40,
                            tooltip=round(sum(marmeleiros)/len(marmeleiros),2),
                            from_y=0,
                            to_y=sum(marmeleiros)/len(marmeleiros),
                            color='#FABFB7',
                            border_radius=0
                        ),
                    ]
                ),
                ft.BarChartGroup(
                    x=4,
                    bar_rods=[
                        ft.BarChartRod(
                            width=40,
                            tooltip=round(sum(externas)/len(externas),2),
                            from_y=0,
                            to_y=sum(externas)/len(externas),
                            color='#FFDA9E',
                            border_radius=0
                        ),
                    ],
                )

            ],
            groups_space=1,
            border=ft.border.all(1,ft.colors.GREY_400),
            left_axis=ft.ChartAxis(
                labels_size=10, title=ft.Text("Volume (Média em ml)"), title_size=20
            ),
            
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0, label=ft.Text("Aroeiras")   
                    ),
                    ft.ChartAxisLabel(
                        value=1, label=ft.Text("Angicos")
                    ),
                    ft.ChartAxisLabel(
                        value=2, label=ft.Text("Juremas")
                    ),
                    ft.ChartAxisLabel(
                        value=3, label=ft.Text("Marmeleiros")
                    ),
                    ft.ChartAxisLabel(
                        value=4, label=ft.Text("Areas Externas")
                    ),
                ],
                labels_size=15,
                labels_interval=20
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
            max_y=max(average)+50,
            interactive=True,
            expand=False,
            
            
        )
        return chart
    except Exception as e:
        print(e)

# def main(page:ft.Page):
#     g = create_chart('12-04-2024')
#     page.add(g)
# ft.app(target=main)