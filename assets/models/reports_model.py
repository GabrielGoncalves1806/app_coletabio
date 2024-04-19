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
    try:
        reports_data = fb_model.get_cloud_data()
        report_list = ft.Column(scroll=True)
        reports_count = 0
        
        
        for collects in reversed(reports_data['coletas']):
            for date in reports_data['coletas'][collects]:
                exp = ft.ExpansionTile(title=ft.Text(date), leading=ft.Icon(ft.icons.CALENDAR_MONTH))
                report_list.controls.append(exp)
                reports_count += 1
                for plant in reports_data['coletas'][collects][date]:
                    exp.controls.append(
                        
                        ft.ListTile(
                            title=ft.Text(f"{plant}:      {reports_data['coletas'][collects][date][plant]} ml"),
                            leading=ft.Icon(ft.icons.FOREST),
                            
                        )
                    )
                    

        return report_list, reports_count
            
    except Exception as e:
        return ft.Text('Sem acesso a internet, verifique a conexão e tente novamente'),0