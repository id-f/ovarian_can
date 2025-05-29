# src/ovarian_can/preprocess/abstract_path_resolver.py
from abc import ABC, abstractmethod
from pathlib import Path

class AbstractPreprocessPathResolver(ABC):

    @abstractmethod
    def get_input_joblib_path(self) -> Path:
        pass

    @abstractmethod
    def get_output_joblib_path(self) -> Path:
        pass

    @abstractmethod
    def get_intermediate_joblib_path(self) -> Path:
        pass

    @abstractmethod
    def get_intermediate_after_PCA_path(self) -> Path:
        pass
    @abstractmethod
    def get_intermediate_after_NN_path(self) -> Path:
        pass
    
