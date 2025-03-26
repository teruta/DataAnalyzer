import os

class File:
    def __init__(self, file_path_dir: str, out_path_dir: str):
        self.file_path_dir = file_path_dir
        self.out_path_dir = out_path_dir
        os.makedirs(self.out_path_dir, exist_ok=True)