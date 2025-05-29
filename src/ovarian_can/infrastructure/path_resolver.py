from ovarian_can.infrastructure.config import BASE_DATA_PATH
from pathlib import Path

class PathResolver:
    def get_raw_data_dir(self) -> Path:
        return BASE_DATA_PATH / "raw" / "Xenium_V1_Human_Ovarian_Cancer_Addon_FFPE_outs"

    def get_interim_data_dir(self) -> Path:
        return BASE_DATA_PATH / "interim"

    def get_processed_data_dir(self) -> Path:
        return BASE_DATA_PATH / "processed"