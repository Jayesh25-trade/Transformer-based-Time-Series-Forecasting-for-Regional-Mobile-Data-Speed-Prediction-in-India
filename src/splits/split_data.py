import os, argparse
import pandas as pd

def run(input_path, outdir, train_ratio=0.8, val_ratio=0.1):
    os.makedirs(outdir, exist_ok=True)
    df = pd.read_csv(input_path, parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    n = len(df)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    n_test = n - n_train - n_val

    train = df.iloc[:n_train]
    val   = df.iloc[n_train:n_train+n_val]
    test  = df.iloc[n_train+n_val:]

    train.to_csv(os.path.join(outdir, "train.csv"), index=False)
    val.to_csv(os.path.join(outdir, "val.csv"), index=False)
    test.to_csv(os.path.join(outdir, "test.csv"), index=False)

    print(f"[INFO] Saved → {outdir}\\train.csv ({len(train)})")
    print(f"[INFO] Saved → {outdir}\\val.csv   ({len(val)})")
    print(f"[INFO] Saved → {outdir}\\test.csv  ({len(test)})")
    print("[DATES]", train.Date.min().date(), "→", test.Date.max().date())

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--train_ratio", type=float, default=0.8)
    ap.add_argument("--val_ratio", type=float, default=0.1)
    args = ap.parse_args()
    run(args.input, args.outdir, args.train_ratio, args.val_ratio)
