import os

import pandas as pd
import re
from sympy import symbols, sympify
import warnings

from ExtractZip import ExtractZip
from GenerateFile import GenerateFile


class DataProcessor:
    def __init__(self, input_transaction_id, input_sheet_name, input_column_list, input_header_data, input_formula = ""):
        self.transaction_id = str(input_transaction_id)
        self.header_data_row = int(input_header_data)
        self.total_sum_e = 0
        self.total_sum_f = 0
        self.total_sum_g = 0
        self.sheet_name = str(input_sheet_name).strip()
        self.column_list = input_column_list
        self.formula = input_formula
        self.failed_files = []
        self.results = []
        self.base_path = os.path.dirname(__file__)
        self.source_path = rf"{self.base_path}/data/exstract/{self.transaction_id}"

    def validate_folder(self):
        result = True
        if not os.path.exists(self.source_path):
            print("Folder tidak ditemukan")
            result = False
        return result

    @staticmethod
    def float_format(value):
        if value == int(value):
            return f"{int(value)}"
        else:
            return f"{value:.3f}".rstrip('0').rstrip('.')

    def read_excel(self, file, engine=None):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return pd.read_excel(file, sheet_name=self.sheet_name, engine=engine, header=self.header_data_row)

    def process_file(self, file_path, file_name, column_list):
        try:
            df = self.read_excel(file_path, "openpyxl")

            missing_columns = [col for col in column_list if col not in df.columns]
            if missing_columns:
                print(f"Kolom berikut tidak ditemukan di file {file_name}: {', '.join(missing_columns)}")
                return

            results_dict = {"File Name": file_name}

            for column in column_list:
                if column in df.columns:
                    df[column] = pd.to_numeric(df[column], errors='coerce')
                    column_sum = df[column].sum(skipna=True)

                    result = column_sum
                    if self.formula is None or self.formula.strip():
                        x = symbols('x')
                        expr = sympify(self.formula)
                        result = expr.subs(x, float(column_sum))

                    results_dict[column] = self.float_format(result)

                    if column == "DC Power PvPV1(W)":
                        self.total_sum_e += result
                    elif column == "DC Power PvPV2(W)":
                        self.total_sum_f += result
                    elif column == "DC Power PvPV3(W)":
                        self.total_sum_g += result
            self.results.append(results_dict)
        except Exception as e:
            self.failed_files.append({"file_name": file_name, "error": str(e)})

    def process_all_files(self):
        for file_name in os.listdir(self.source_path):
            if file_name.endswith(".xlsx"):
                file_path = os.path.join(self.source_path, file_name)
                self.process_file(file_path, file_name, self.column_list)

    def sort_results(self):
        def extract_number(file_name):
            match = re.search(r'\((\d+)\)', file_name)
            return int(match.group(1)) if match else float('inf')

        self.results = sorted(self.results, key=lambda x: extract_number(x["File Name"]))


    def display_failed_files(self):
        if self.failed_files:
            print("\nFile yang gagal diproses:")
            for item in self.failed_files:
                print(f"File: {item['file_name']}, Error: {item['error']}")
        else:
            print("\nSemua file berhasil diproses.")

    def run(self):
        # extract = ExtractZip(self.transaction_id)
        # extract.run()

        status = self.validate_folder()
        if status:
            self.process_all_files()
            self.sort_results()
            self.display_failed_files()

            generate_file = GenerateFile(self.results, self.transaction_id, self.column_list)
            generate_file.generate_graph()
            generate_file.generate_excel()

            # extract.rm_file_and_folder()

if __name__ == "__main__":
    # ex = "DC Power PvPV1(W), DC Power PvPV2(W), DC Power PvPV3(W)"
    ex = "DC Power PvPV1(W)"
    name = "Inverter History Report_SMSolar"
    a = input("Masukkan id: ")
    b = [col.strip() for col in ex.split(',')]
    c = input("Masukkan row number: ")
    proses = DataProcessor(a, name, b, c)
    proses.run()
