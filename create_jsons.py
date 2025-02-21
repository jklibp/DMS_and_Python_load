import json
import pandas as pd

def update_rule_ids_from_excel(input_excel_path, input_json_path, output_json_path):

    excel_data = pd.read_excel(input_excel_path)

    with open(input_json_path, 'r') as file:
        data = json.load(file)

    column_exists = 'Tabla' in excel_data.columns

    if 'rules' in data:
        # Recorrer las reglas y asignar IDs auto-incrementales
        for idx, rule in enumerate(data['rules'], start=1):
            rule['rule-id'] = str(idx)
            if column_exists and idx - 1 < len(excel_data):
                rule['rule-name'] = 'include_' + excel_data.iloc[idx - 1]['Tabla']

            if column_exists and idx - 1 < len(excel_data):
                rule['object-locator']['table-name'] = excel_data.iloc[idx - 1]['Tabla']
                                                             
    with open(output_json_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Archivo actualizado guardado en: {output_json_path}")

input_excel_path = "tablas_fin.xlsx"  # Reemplaza con la ruta de tu archivo Excel
input_json_path = "primeras_3000_auto_increment.json"  # Reemplaza con la ruta de tu archivo JSON original
output_json_path = "output.json"  # Reemplaza con la ruta de salida deseada

update_rule_ids_from_excel(input_excel_path, input_json_path, output_json_path)
