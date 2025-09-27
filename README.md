#  Transformer-based Time Series Forecasting for Regional Mobile Data Speed Prediction in India  

This project predicts **regional mobile internet speeds in India** using **transformer-based time series models**:  

-  **Temporal Fusion Transformer (TFT)**  
   **Informer** (coming soon)  

The dataset is sourced from [data.gov.in](https://www.data.gov.in/resource/month-wise-all-india-crowdsourced-mobile-data-speed-measurement), containing **crowdsourced mobile internet speed test records**.  

---

##  Project Structure  

```text
mobile-speed-forecast/
├─ data/
│  ├─ raw/          <- raw CSVs (ignored in git, keep locally)
│  ├─ interim/      <- intermediate processing (ignored in git)
│  └─ processed/    <- cleaned datasets, features, splits
├─ src/
│  ├─ data/         <- cleaning scripts
│  ├─ features/     <- feature engineering
│  ├─ splits/       <- train/val/test split
│  ├─ models/       <- training + evaluation
│  └─ app/          <- Streamlit UI
├─ .gitignore
├─ requirements.txt
└─ README.md
```
##  Clone the repository  

```bash
git clone https://github.com/Jayesh25-trade/Transformer-based-Time-Series-Forecasting-for-Regional-Mobile-Data-Speed-Prediction-in-India.git
cd Transformer-based-Time-Series-Forecasting-for-Regional-Mobile-Data-Speed-Prediction-in-India
```
```bash

 Create virtual environment
python -m venv .venv
. .venv\Scripts\Activate.ps1   # Windows PowerShell
```
 Install requirements
```bash

pip install --upgrade pip
pip install -r requirements.txt
```
 Workflow
🔹 Step 1. Data Cleaning
```bash

python src/data/clean_speed_data.py \
  --input data/raw/merged_output.csv \
  --outdir data/processed
```

🔹 Step 2. Feature Engineering
```bash

python src/features/feature_engineering.py \
  --input data/processed/cleaned_data_with_date.csv \
  --outdir data/processed
```

🔹 Step 3. Train/Val/Test Split
```bash

python src/splits/split_data.py \
  --input data/processed/features.csv \
  --outdir data/processed
```

🔹 Step 4. Train TFT Model
```bash

Install extra dependencies:

pip install torch==2.3.1 lightning==2.3.3 pytorch-forecasting==1.4.0 "torchmetrics>=1.3,<2"
```
```bash

Train:
```
```bash

python src/models/train_tft.py \
  --train data/processed/train.csv \
  --val data/processed/val.csv \
  --outdir models \
  --max_epochs 5 --max_enc_len 6 --max_pred_len 1
```

🔹 Step 5. Train Informer Model (Coming Soon)
```bash

```

🔹 Step 6. Evaluation
```bash

python src/models/evaluate.py \
  --test data/processed/test.csv \
  --models models/
```
```bash

🔹 Step 7. Visualization
python src/visualization/plots.py
```
🔹Step 8. Streamlit App
```bash
streamlit run src/app/streamlit_app.py
```
