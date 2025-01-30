import os
import pandas as pd
import matplotlib.pyplot as plt

class GenerateFile:
    def __init__(self, input_data, input_folder_name, input_list_columns):
        self.data = input_data
        self.list_columns = input_list_columns
        self.folder_name = input_folder_name
        self.base_path = os.path.dirname(__file__)
        self.result_img_path   = f"{self.base_path}/data/results/img/grafik_{self.folder_name}.png"
        self.result_excel_path = rf"{self.base_path}/data/results/excel/hasil_perhitungan_{self.folder_name}.xlsx"

        self.validate_path()

    def validate_path(self):
        if not os.path.exists(f"{self.base_path}/data/results/img"):
            os.makedirs(f"{self.base_path}/data/results/img")
        if not os.path.exists(f"{self.base_path}/data/results/excel"):
            os.makedirs(f"{self.base_path}/data/results/excel")

    def generate_graph(self):
        df_results = pd.DataFrame(self.data)
        label_x = df_results["File Name"].str.replace('.xlsx', '', regex=False)
        plt.figure(figsize=(10, 6))
        for column in self.list_columns:
            df_results[column] = pd.to_numeric(df_results[column], errors='coerce')
            plt.plot(label_x, df_results[column], label=column, marker='.')
        plt.title(f"Data {self.folder_name}".upper())
        plt.xlabel('Sumbu X')
        plt.ylabel('Sumbu Y')
        plt.xticks(rotation=90)
        plt.subplots_adjust(bottom=0.3)
        plt.legend()
        plt.grid()
        plt.savefig(self.result_img_path)
        plt.close()

    def generate_excel(self):
        if os.path.exists(self.result_excel_path):
            os.remove(self.result_excel_path)

        df_results = pd.DataFrame(self.data)
        print(df_results)
        missing_columns = [col for col in self.list_columns if col not in df_results.columns]
        if missing_columns:
            raise ValueError(f"The following columns are missing: {missing_columns}")

        total_sums = {f"Total {col}": [df_results[col].sum()] for col in missing_columns}

        df_total = pd.DataFrame(total_sums)

        with pd.ExcelWriter(self.result_excel_path, engine='openpyxl') as writer:
            df_results.to_excel(writer, sheet_name="Hasil File", index=False)
            df_total.to_excel(writer, sheet_name="Hasil Total File", index=False)