import os
import zipfile
import shutil

class ExtractZip:
    def __init__(self, input_id_file):
        self.id_file = input_id_file
        self.base_path = os.path.dirname(__file__)
        self.zip_path = f"{self.base_path}/data/upload/{self.id_file}.zip"
        self.result_path = rf"{self.base_path}/data/exstract/"

    def rm_file_and_folder(self):
        os.remove(self.zip_path)
        shutil.rmtree(f"{self.result_path}{self.id_file}")

    def validate_paths(self):
        if not os.path.exists(self.zip_path):
            raise FileNotFoundError(f"File ZIP '{self.zip_path}' tidak ditemukan.")

        if os.path.exists(rf"{self.result_path}{self.id_file}"):
            shutil.rmtree(rf"{self.result_path}{self.id_file}")

        if not os.path.exists(self.result_path):
            os.makedirs(self.result_path)

    def extract(self):
        temp_extract_path = os.path.join(self.result_path, "temp_extraction")
        os.makedirs(temp_extract_path, exist_ok=True)

        with zipfile.ZipFile(self.zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_extract_path)

        extracted_items = os.listdir(temp_extract_path)
        if len(extracted_items) == 1 and os.path.isdir(os.path.join(temp_extract_path, extracted_items[0])):
            extracted_folder = os.path.join(temp_extract_path, extracted_items[0])
        else:
            extracted_folder = temp_extract_path

        final_folder = os.path.join(self.result_path, self.id_file)

        shutil.move(extracted_folder, final_folder)
        print(f"Folder berhasil diekstrak dan diganti nama menjadi: {final_folder}")

        if os.path.exists(temp_extract_path):
            shutil.rmtree(temp_extract_path)

    def run(self):
        try:
            self.validate_paths()
            self.extract()
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

