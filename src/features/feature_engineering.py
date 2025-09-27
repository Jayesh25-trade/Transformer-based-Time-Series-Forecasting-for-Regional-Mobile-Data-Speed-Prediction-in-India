import os
import argparse
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

def run(input_path, outdir, outname="features"):
    os.makedirs(outdir, exist_ok=True)

    # Load cleaned data
    df = pd.read_csv(input_path, parse_dates=["Date"])

    # Encode categorical columns
    cat_cols = ["service_provider", "circle", "tech"]
    encoders = {}
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
        joblib.dump(le, os.path.join(outdir, f"{col}_encoder.pkl"))

    # Scale numeric columns
    num_cols = ["download", "upload", "signal_strength"]
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    joblib.dump(scaler, os.path.join(outdir, "scaler.pkl"))

    # Save processed features
    out_csv = os.path.join(outdir, f"{outname}.csv")
    df.to_csv(out_csv, index=False)
    print(f"[INFO] Saved processed features → {out_csv}")
    print(df.head())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Path to cleaned_data_with_date.csv")
    ap.add_argument("--outdir", required=True, help="Folder to save processed features")
    args = ap.parse_args()

    run(args.input, args.outdir)

if __name__ == "__main__":
    main()
