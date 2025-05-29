import anndata as ad
from pathlib import Path

def load_anndata(h5ad_path: Path) -> ad.AnnData:
    return ad.read_h5ad(h5ad_path)

def save_anndata(adata: ad.AnnData, h5ad_path: Path):
    adata.write(h5ad_path)
