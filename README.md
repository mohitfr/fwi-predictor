# FireWatch — Fire Danger Assessment Tool

A field tool for forest fire officials to assess daily fire danger from weather and fuel moisture readings. Built as a learning project to take a regression model from notebook to a deployed, usable application.

## Overview

FireWatch predicts the Fire Weather Index (FWI) from seven field readings and translates it into a plain danger rating with a recommended action — built for someone in the field, not a data scientist.

## Live Demo

http://firewatch-env.eba-kbuhcs4b.ap-south-1.elasticbeanstalk.com

> Note: Running on HTTP — HTTPS and custom domain pending.

## Pages

| Page | Route | Purpose |
|------|-------|---------|
| Overview | `/` | What the tool does, danger scale, how to use it |
| New Assessment | `/assess` (GET) | Input form for today's readings |
| Submit Assessment | `/assess` (POST) | Validates and processes input |
| Result | `/result` | Danger rating and recommended action |

## Project Structure

```
fwi-predictor/
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── datasets/
│   │   ├── algerian_forest_fires.csv
│   │   └── algerian_forest_fire_cleaned.csv
│   ├── eda_data_prep.ipynb
│   └── model.ipynb
│
├── static/
│   └── css/
│       ├── base.css
│       ├── home.css
│       ├── assess.css
│       ├── result.css
│       └── notfound.css
│
├── templates/
│   ├── index.html
│   ├── assess.html
│   ├── result.html
│   └── 404.html
│
├── application.py
├── config.py
├── predictor.py
├── validators.py
│
├── .gitignore
├── Procfile
├── .ebextensions/
│   └── python.config
├── README.md
└── requirements.txt
```

## Why this structure

- **`models/`** — only the trained `.pkl` outputs, nothing else
- **`notebooks/`** — all research: EDA, cleaning, training, in order
- **`config.py`** — every field's label, unit, valid range, and the risk bands, in one place
- **`predictor.py`** — wraps the model so `application.py` never touches pickle/pandas directly
- **`validators.py`** — checks required fields, type, and valid ranges with clear error messages
- **`application.py`** — routing only. Named `application.py` to match AWS Elastic Beanstalk's default Python platform convention
- Each page has its own stylesheet under `static/css/`, plus a shared `base.css` for nav, footer, and buttons

## Run Locally

```bash
pip install -r requirements.txt
python application.py
```

Visit `http://localhost:5000`

## Input Validation

Every field is checked for:
- Presence (required)
- Numeric type
- Valid range (defined per-field in `config.py`)

Invalid submissions return to the form with the original values preserved and clear error messages.

## Danger Rating Bands

| FWI | Rating | Recommended Action |
|-----|--------|---------------------|
| 0 – 5 | Low | Routine monitoring is sufficient |
| 5 – 12 | Moderate | Increase patrol frequency in dry zones |
| 12 – 20 | High | Restrict open burning, brief field crews |
| 20+ | Very High | Issue public advisory, pre-position response teams |

## Model

Ridge Regression trained on the Algerian Forest Fires dataset (UCI/Kaggle, 2012). Features: Temperature, Relative Humidity, Wind Speed, Rainfall, FFMC, DMC, ISI. See `notebooks/` for EDA and training details.

## Acknowledgements

The EDA, data cleaning, and model training in `notebooks/` are my own work. For this project, I worked with Claude (Anthropic) to help structure the Flask backend (`config.py`, `predictor.py`, `validators.py`) and to speed up the frontend build (HTML/CSS), since I wanted to focus my time on the ML side. I have prior experience building full Flask applications with HTML, CSS, and JS, so I reviewed, tested, and adjusted everything here myself before including it in the repo.