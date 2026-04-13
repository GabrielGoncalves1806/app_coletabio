import flet as ft
import flet_charts as ftc
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

        species = [
            ('Aroeiras', aroeiras, '#B2E2F2'),
            ('Angicos', angicos, '#B0C2F2'),
            ('Juremas', juremas, '#CAACF9'),
            ('Marmeleiros', marmeleiros, '#FABFB7'),
            ('Areas Externas', externas, '#FFDA9E'),
        ]
        averages = [sum(values)/len(values) if values else 0 for _, values, _ in species]

        groups = []
        labels = []
        for i, ((name, _, color), avg) in enumerate(zip(species, averages)):
            groups.append(
                ftc.BarChartGroup(
                    x=i,
                    rods=[
                        ftc.BarChartRod(
                            width=40,
                            tooltip=ftc.BarChartRodTooltip(
                                text=str(round(avg, 2)),
                                text_style=ft.TextStyle(color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                            ),
                            from_y=0,
                            to_y=avg,
                            color=color,
                            border_radius=0,
                        ),
                    ],
                )
            )
            labels.append(
                ftc.ChartAxisLabel(
                    value=i,
                    label=ft.Container(
                        content=ft.Text(name, size=12),
                        rotate=ft.Rotate(-0.6, alignment=ft.Alignment.CENTER),
                        padding=ft.Padding.only(top=20),
                    ),
                )
            )

        max_value = max(averages) + 50
        y_step = max(round(max_value / 5), 1)
        y_labels = [
            ftc.ChartAxisLabel(value=i * y_step, label=ft.Text(str(i * y_step), size=11))
            for i in range(6)
        ]

        chart = ftc.BarChart(
            groups=groups,
            tooltip=ftc.BarChartTooltip(
                bgcolor=ft.Colors.BLACK87,
                border_radius=6,
                padding=8,
            ),
            group_spacing=24,
            border=ft.Border.all(1, ft.Colors.GREY_400),
            left_axis=ftc.ChartAxis(
                title=ft.Text("Volume (Média em ml)"),
                title_size=20,
                label_size=40,
                labels=y_labels,
                show_min=False,
                show_max=False,
            ),
            bottom_axis=ftc.ChartAxis(
                labels=labels,
                label_size=50,
            ),
            horizontal_grid_lines=ftc.ChartGridLines(
                color=ft.Colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            max_y=max_value,
            interactive=True,
            height=400,
        )
        return chart
    except Exception as e:
        print(f'create_chart error: {e}')
        return ft.Text(f'Erro ao gerar gráfico: {e}')

# def main(page:ft.Page):
#     g = create_chart('12-04-2024')
#     page.add(g)
# ft.app(target=main)