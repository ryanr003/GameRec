import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

# Load dataset:
file_path = "steam-200k.csv" 
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "tamber/steam-video-games",
    file_path,
)

