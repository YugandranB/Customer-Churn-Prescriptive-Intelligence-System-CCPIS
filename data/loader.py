import pandas as pd
import kagglehub
import os

def load_retail_dataset():
    path = kagglehub.dataset_download("mashlyn/online-retail-ii-uci")
    csv_file_path = os.path.join(path, "online_retail_II.csv")
    df = pd.read_csv(csv_file_path)
    return df
