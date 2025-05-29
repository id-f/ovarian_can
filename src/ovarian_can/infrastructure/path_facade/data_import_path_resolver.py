from ovarian_can.data_import.abstract_path_resolver import AbstractDataImportPathResolver
from ovarian_can.infrastructure.path_resolver import PathResolver
from pathlib import Path

class DataImportPathResolver(AbstractDataImportPathResolver):
    def __init__(self):
        self.resolver = PathResolver()

    def get_input_h5_path(self) -> Path:
        return self.resolver.get_raw_data_dir() / "cell_feature_matrix.h5"

    def get_cells_csv_gz_path(self) -> Path:
        return self.resolver.get_raw_data_dir() / "cells.csv.gz"

    def get_decompressed_csv_path(self) -> Path:
        return self.resolver.get_interim_data_dir() / "cells.csv"

    def get_output_joblib_path(self) -> Path:
        return self.resolver.get_interim_data_dir() / "xenium_ovarian_cancer_preprocessed.joblib"
