from data.loader import load_retail_dataset
from features.behavioral_engine import build_behavioral_features
from models.segmentation import apply_segmentation
from models.churn_model import train_churn_model
from dashboard.ui import launch_dashboard

def main():

    df = load_retail_dataset()

    rfm = build_behavioral_features(df)

    rfm = apply_segmentation(rfm)

    model = train_churn_model(rfm)

    launch_dashboard(model, rfm)

if __name__ == "__main__":
    main()
