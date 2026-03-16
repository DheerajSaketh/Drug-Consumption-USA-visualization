# Drug Consumption USA Visualization

## 📌 Problem
Making sense of complex U.S. drug overdose data to identify high-risk states, trends over time, and regions that need public safety attention.

## ✅ Solution
An interactive visualization project (in the style of a Tableau dashboard) that provides:
- **Geospatial mapping** (state-level choropleths) to show hotspots
- **Temporal analysis** (year-over-year trends) with interactive sliders
- **State-level comparisons** to surface top impacted areas

## 🛠 Tools & Technologies
- Python (Pandas, NumPy)
- Plotly (interactive charts + maps)
- Matplotlib + Seaborn (static charts)
- Dash (interactive dashboard UI)

## 📥 Data Source
CDC Provisional Drug Overdose Death Counts: https://data.cdc.gov/NCHS/VSRR-Provisional-Drug-Overdose-Death-Counts/xkb8-kh2a

## ⚙️ Setup
Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## ▶️ Run Scripts
### 1) Script-based outputs (static + interactive HTML)
```bash
python main.py
```
Outputs:
- `drug_overdose_deaths.html` (interactive Plotly chart)
- `drug_overdose_deaths.png` (static Matplotlib chart)

### 2) Interactive dashboard (Dash)
```bash
python app.py
```
Then open the URL shown in the terminal (usually `http://127.0.0.1:8050`).

## 📦 Project Files
- `main.py` — batch script that loads data and saves charts
- `app.py` — interactive Dash dashboard
- `exploration.ipynb` — exploratory notebook with step-by-step analysis
- `requirements.txt` — dependency list
- `.gitignore` — ignores generated artifacts

## 🧩 Notes
This project is intended for learning and exploration. Data is public and results should be interpreted cautiously.