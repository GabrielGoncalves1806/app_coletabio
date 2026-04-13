from assets.models import fb_model
import flet as ft

# Função não utilizada por escolha do usuário

# def generate_datatable():

#     data_table = ft.DataTable(
#             columns=[
#                 ft.DataColumn(ft.Text('Data coleta')),
#                 ft.DataColumn(ft.Text('Especie')),
#                 ft.DataColumn(ft.Text('Milimetros'),numeric=True)
#                 ],
#                 rows=[],
#                 show_bottom_border=True
                
#             )
    
#     reports_data = fb_model.get_cloud_data()
#     for data in reports_data['coletas']:
#         for date in reports_data['coletas'][data]:
#             for planta in reports_data['coletas'][data][date]:
#                 data_table.rows.append(ft.DataRow(
#                     cells=[
#                         ft.DataCell(ft.Text(date)),
#                         ft.DataCell(ft.Text(planta)),
#                         ft.DataCell(ft.Text(reports_data['coletas'][data][date][planta]))
#                         ]
#                     )
#                 )

# Função que gera a lista de relatório

def get_reports_list():
    report_list = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    reports_count = 0
    try:
        reports_data = fb_model.get_cloud_data()
        if not reports_data or 'coletas' not in reports_data:
            report_list.controls.append(
                ft.Text('Sem acesso a internet ou nenhuma coleta encontrada.')
            )
            return report_list, 0

        for collects in reversed(list(reports_data['coletas'])):
            for date in reports_data['coletas'][collects]:
                children = []
                for plant in reports_data['coletas'][collects][date]:
                    children.append(
                        ft.ListTile(
                            title=ft.Text(f"{plant}: {reports_data['coletas'][collects][date][plant]} ml"),
                            leading=ft.Icon(ft.Icons.FOREST),
                        )
                    )
                report_list.controls.append(
                    ft.ExpansionTile(
                        title=ft.Text(date),
                        leading=ft.Icon(ft.Icons.CALENDAR_MONTH),
                        controls=children,
                    )
                )
                reports_count += 1
        return report_list, reports_count

    except Exception as e:
        report_list.controls.append(
            ft.Text(f'Erro ao carregar relatórios: {e}')
        )
        return report_list, 0