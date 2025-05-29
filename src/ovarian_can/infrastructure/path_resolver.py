from ovarian_can.infrastructure.config import BASE_DATA_PATH
from pathlib import Path

class PathResolver:
    def get_raw_data_dir(self) -> Path:
        return BASE_DATA_PATH / "raw" / "Xenium_Prime_Ovarian_Cancer_FFPE_XRrun_outs"

    def get_interim_data_dir(self) -> Path:
        return BASE_DATA_PATH / "interim"

    def get_processed_data_dir(self) -> Path:
        return BASE_DATA_PATH / "processed"