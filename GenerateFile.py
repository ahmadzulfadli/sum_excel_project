import os
import pandas as pd
import matplotlib.pyplot as plt

class GenerateFile:
    def __init__(self, input_data, input_folder_name):
        self.data = input_data
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
        plt.plot(label_x, df_results["DC Power PvPV1(W)"], label='PvPV1', marker='o')
        plt.plot(label_x, df_results["DC Power PvPV2(W)"], label='PvPV2', marker='o')
        plt.plot(label_x, df_results["DC Power PvPV3(W)"], label='PvPV3', marker='o')
        plt.title('DC Power Harian')
        plt.xlabel('File Name')
        plt.ylabel('DC Power (W)')
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
        total_sum_pv1 = df_results["DC Power PvPV1(W)"].sum()
        total_sum_pv2 = df_results["DC Power PvPV2(W)"].sum()
        total_sum_pv3 = df_results["DC Power PvPV3(W)"].sum()

        with pd.ExcelWriter(self.result_excel_path, engine="openpyxl") as writer:
            df_results.to_excel(writer, sheet_name="Hasil Harian", index=False)
            df_bulanan = pd.DataFrame({
                "Total DC Power PvPV1(W)": [total_sum_pv1],
                "Total DC Power PvPV2(W)": [total_sum_pv2],
                "Total DC Power PvPV3(W)": [total_sum_pv3]
            })
            df_bulanan.to_excel(writer, sheet_name="Hasil Bulanan", index=False)