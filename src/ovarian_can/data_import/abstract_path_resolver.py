from abc import ABC, abstractmethod
from pathlib import Path

class AbstractDataImportPathResolver(ABC):

    @abstractmethod
    def get_input_h5_path(self) -> Path:
        pass

    @abstractmethod
    def get_cells_csv_gz_path(self) -> Path:
        pass

    @abstractmethod
    def get_decompressed_csv_path(self) -> Path:
        pass

    @abstractmethod
    def get_output_joblib_path(self) -> Path:
        pass
