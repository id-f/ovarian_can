from ovarian_can.preprocess.abstract_path_resolver import AbstractPreprocessPathResolver
from ovarian_can.infrastructure.path_resolver import PathResolver
from pathlib import Path

class PreprocessPathResolver(AbstractPreprocessPathResolver):
    def __init__(self):
        self.resolver = PathResolver()

    def get_input_joblib_path(self) -> Path:
        return self.resolver.get_interim_data_dir() / "xenium_ovarian_cancer_preprocessed.joblib"

    def get_output_joblib_path(self) -> Path:
        return self.resolver.get_processed_data_dir() / "xenium_ovarian_cancer_after_preprocessing.joblib"

    def get_intermediate_joblib_path(self) -> Path:
        return self.resolver.get_interim_data_dir() / "intermediate_after_scale.joblib"
    
    def get_intermediate_after_PCA_path(self) -> Path:
        return self.resolver.get_interim_data_dir() / "intermediate_after_PCA.joblib"
    
    def get_intermediate_after_NN_path(self) -> Path:
        return self.resolver.get_interim_data_dir() / "intermediate_after_NN.joblib"