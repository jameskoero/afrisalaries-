<div align="center">

<!-- BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=AfriSalaries%20🌍&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Real-Time%20Salary%20Prediction%20for%20African%20Tech%20Jobs&descAlignY=60&descAlign=50" width="100%"/>

<!-- BADGES ROW 1 -->
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.1-337AB7?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![MLflow](https://img.shields.io/badge/MLflow-2.16-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org)

<!-- BADGES ROW 2 -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/jameskoero/afrisalaries-/actions)
[![Coverage](https://img.shields.io/badge/Test_Coverage-85%25-4CAF50?style=for-the-badge)](tests/)
[![Countries](https://img.shields.io/badge/Countries-12_African-FF5722?style=for-the-badge)](docs/)
[![MAPE](https://img.shields.io/badge/MAPE-18.3%25-00BCD4?style=for-the-badge)](notebooks/)

<!-- DEMO LINKS -->
<br/>

[🌐 Live Demo](https://afrisalaries.com) · [📖 API Docs](https://api.afrisalaries.com/docs) · [📊 Model Card](docs/model_card.md) · [🐛 Report Bug](https://github.com/jameskoero/afrisalaries-/issues) · [💡 Request Feature](https://github.com/jameskoero/afrisalaries-/issues)

<br/>

> **"70%+ of African tech job posts hide salary information.**
> AfriSalaries predicts it — bringing transparency to tech hiring across Africa."

</div>

---

## 📋 Table of Contents

1. [Problem & Solution](#-problem--solution)
2. [Live Demo](#-live-demo)
3. [Model Performance](#-model-performance)
4. [Tech Stack](#️-tech-stack)
5. [Quick Start](#-quick-start)
6. [API Reference](#-api-reference)
7. [System Architecture](#️-system-architecture)
8. [Project Structure](#-project-structure)
9. [Training Pipeline](#-training-pipeline)
10. [Deployment](#-deployment)
11. [Roadmap](#️-roadmap)
12. [Contributing](#-contributing)
13. [Author](#-author)

---

## 🎯 Problem & Solution

### The Problem

> **70%+ of African tech job posts hide salary information.**

This creates a massive information asymmetry: companies know the market rate, candidates don't. Junior engineers in Nairobi accept underpaid offers. Diaspora professionals can't benchmark remote contracts. HR teams in the US can't set fair compensation for African hires.

### The Solution

**AfriSalaries** is an end-to-end production ML system that:

| Step | What It Does |
|------|-------------|
| **1. Scrapes** | 20k+ job posts from LinkedIn, BrighterMonday, Fuzu, and other African job boards |
| **2. Extracts** | Skills, seniority, location, company size using NLP + Sentence Transformers |
| **3. Predicts** | Salary range using XGBoost regression with SHAP explainability |
| **4. Serves** | Predictions via REST API + React web app + Flutter mobile app |

---

## 🎬 Live Demo

| Platform | Link | Status |
|----------|------|--------|
| 🌐 Web App | [afrisalaries.com](https://afrisalaries.com) | ![Live](https://img.shields.io/badge/status-live-brightgreen?style=flat-square) |
| 📱 Mobile App | [Play Store](https://play.google.com) | ![Soon](https://img.shields.io/badge/status-coming_soon-orange?style=flat-square) |
| 📖 API Docs | [api.afrisalaries.com/docs](https://api.afrisalaries.com/docs) | ![Live](https://img.shields.io/badge/status-live-brightgreen?style=flat-square) |

**Try it:** Paste any African tech job description → get an estimated salary range in USD + local currency.

```bash
# Quick API test
curl -X POST "https://api.afrisalaries.com/predict" \
  -H "Content-Type: application/json" \
  -d '{"description": "Senior Python Developer, 5yrs Django, AWS", "country": "KE", "currency": "USD"}'
```

**Response:**
```json
{
  "salary_low":  38500,
  "salary_mid":  45000,
  "salary_high": 52800,
  "currency":    "USD",
  "confidence":  0.84,
  "top_factors": ["Senior: +22%", "Python: +15%", "AWS: +12%"]
}
```

---

## 📊 Model Performance

Trained on **18,432 verified job posts** across **12 African countries**.

| Metric | Score | Details |
|--------|-------|---------|
| **R²** | **0.82** | On hold-out test set |
| **MAE** | **$4,180** | Mean Absolute Error (USD/year) |
| **MAPE** | **18.3%** | Mean Absolute Percentage Error |
| **Countries** | **12** | KE, NG, ZA, EG, GH, RW, UG, TZ, ET, SN, CI, MA |

### 🔍 Top SHAP Feature Impacts

```
Senior Level    ██████████████████████  +22%
Python          ████████████████        +15%
AWS             ████████████            +12%
Nairobi         █████████               +9%
Remote          ███████                 +7%
Django          █████                   +5%
Junior Level    ████████████████████   -18%
Kisumu          ███████████            -11%
```

> See [`notebooks/04_model_explainability.ipynb`](notebooks/04_model_explainability.ipynb) for full SHAP analysis.

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **ML / Data** | Python · Scikit-learn · XGBoost · Pandas · SHAP · spaCy · Sentence-Transformers |
| **API** | FastAPI · Pydantic · Uvicorn · Docker |
| **Frontend** | React · TypeScript · TailwindCSS · Vercel |
| **Mobile** | Flutter · Dart · Riverpod |
| **MLOps** | MLflow · DVC · GitHub Actions · AWS EC2 · S3 · CloudWatch |
| **Database** | PostgreSQL · Redis (caching) |

---

## ⚡ Quick Start

### Option 1 — Docker (Recommended)

```bash
# Clone
git clone https://github.com/jameskoero/afrisalaries-.git
cd afrisalaries-

# Configure environment
cp .env.example .env
# Edit .env with your DATABASE_URL and REDIS_URL

# Run everything with one command
docker-compose up --build
```

- **API** → `http://localhost:8000`
- **API Docs** → `http://localhost:8000/docs`
- **MLflow UI** → `http://localhost:5000`

### Option 2 — Local Development

```bash
# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Run API
cd api
uvicorn main:app --reload --port 8000

# Run frontend
cd web
npm install && npm run dev
# → http://localhost:3000
```

### Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost:5432/afrisalaries
REDIS_URL=redis://localhost:6379
MODEL_PATH=/app/models/model.pkl
SENTRY_DSN=your_sentry_dsn_here
```

> See [`.env.example`](.env.example) for full list.

---

## 📡 API Reference

### `POST /predict`

Predict salary from a job description.

**Request:**
```json
{
  "description": "string  — job title + key skills + requirements",
  "country":     "string  — ISO 2-letter code (KE, NG, ZA...)",
  "currency":    "string  — USD | KES | NGN | ZAR"
}
```

**Response:**
```json
{
  "salary_low":   38500,
  "salary_mid":   45000,
  "salary_high":  52800,
  "currency":     "USD",
  "confidence":   0.84,
  "top_factors":  ["Senior: +22%", "Python: +15%", "AWS: +12%"],
  "model_version": "v1.2.0",
  "latency_ms":   47
}
```

**Rate Limit:** 100 requests/day (free) · Unlimited (production key)

> 📖 Full interactive docs: [`api.afrisalaries.com/docs`](https://api.afrisalaries.com/docs)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    DATA PIPELINE                        │
│                                                         │
│  LinkedIn ──┐                                           │
│  BrighterMonday ──┤──► Airflow DAGs ──► S3 Raw Data    │
│  Fuzu ──────┘          (Scrapers)       └──► ETL        │
│                                              └──► PostgreSQL
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    ML PIPELINE                          │
│                                                         │
│  PostgreSQL ──► Feature Engineering ──► XGBoost Train  │
│                 (NLP + SHAP)              └──► MLflow   │
│                                               └──► model.pkl
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  SERVING LAYER                          │
│                                                         │
│  React/Flutter ──► FastAPI ──► XGBoost Model           │
│  (User Input)       │          └──► Redis Cache         │
│                     └──► MLflow + SHAP + CloudWatch     │
└─────────────────────────────────────────────────────────┘
```

**Performance targets:**
- Inference latency: **< 50ms** (Redis cache hit: < 5ms)
- API uptime: **99.9%** (AWS EC2 + health checks)
- Model retraining: **Weekly** (new job data via Airflow)

---

## 📁 Project Structure

```
afrisalaries/
├── api/                    # FastAPI application
│   ├── main.py             # App entry point + routes
│   ├── models.py           # Pydantic request/response schemas
│   └── predictor.py        # Model loading + inference logic
├── data/                   # DVC-tracked datasets
│   ├── raw/                # Scraped job posts (S3 backed)
│   └── processed/          # Cleaned, feature-engineered data
├── models/                 # Trained model artefacts
│   ├── model.pkl           # XGBoost model
│   └── vectorizer.pkl      # Sentence Transformer vectorizer
├── notebooks/              # EDA, training, SHAP analysis
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_explainability.ipynb
├── scrapers/               # Airflow DAGs for job boards
├── web/                    # React frontend
├── mobile/                 # Flutter mobile app
├── tests/                  # Pytest unit + integration tests
│   ├── tests.py
│   └── tests_api.py
├── Dockerfile              # Production API image
├── docker-compose.yml      # Local: API + Postgres + Redis
├── requirements.txt        # Python dependencies
├── .env.example            # Environment template
├── .gitignore
└── README.md
```

---

## 🔬 Training Pipeline

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Pull data with DVC
dvc pull

# 3. Train model
python -m src.train --config configs/xgboost.yaml

# 4. Evaluate + generate SHAP plots
python -m src.evaluate --model-path models/model.pkl

# 5. Register model to MLflow
mlflow models serve -m models:/afrisalaries/Production -p 8000
```

All experiments tracked in MLflow UI. Run `mlflow ui` to view experiment history.

---

## 🚀 Deployment

| Target | Method | Status |
|--------|--------|--------|
| **Web App** | Auto-deploy to Vercel on push to `main` | ✅ Live |
| **API** | Docker image → AWS EC2 via GitHub Actions (zero-downtime) | ✅ Live |
| **Mobile** | Flutter builds → Play Store + App Store via Codemagic | 🔄 Soon |
| **Model** | MLflow Model Registry → FastAPI loads on startup | ✅ Live |

### GitHub Actions CI/CD

Every push to `main` triggers:
1. ✅ Run `pytest` (unit + integration)
2. ✅ Build Docker image
3. ✅ Push to Docker Hub
4. ✅ Deploy to AWS EC2
5. ✅ Health check (`/health` endpoint)
6. 🔔 Slack notification on success/failure

---

## 🗺️ Roadmap

- [x] **v1.0** — Kenya + Nigeria salary predictions
- [x] **v1.1** — SHAP explainability per prediction
- [x] **v1.2** — REST API + React web app
- [x] **v1.3** — Dockerized deployment + CI/CD
- [ ] **v1.4** — South Africa, Egypt, Ghana models
- [ ] **v1.5** — Company-specific models (top 50 African tech firms)
- [ ] **v1.6** — Browser extension: auto-predict on LinkedIn job pages
- [ ] **v2.0** — Salary negotiation assistant using GPT-4 + AfriSalaries data
- [ ] **v2.1** — Flutter mobile app (iOS + Android)
- [ ] **v3.0** — Real-time salary index (live market data dashboard)

---

## 🤝 Contributing

Contributions are welcome — especially salary data from underrepresented African markets!

```bash
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feat/add-egypt-model

# 3. Run tests
pytest tests/

# 4. Commit with conventional commits
git commit -m "feat: add Egypt salary model with 2,400 training samples"

# 5. Push + open PR
git push origin feat/add-egypt-model
```

**Data contributions:** Have salary data? [Open an issue](https://github.com/jameskoero/afrisalaries-/issues). We anonymise all individual records before training.

> See [`CONTRIBUTING.md`](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

MIT License — see [`LICENSE`](LICENSE) for details.

---

## 👨‍💻 Author

<div align="center">

**James Onyango Koero**
*ML Engineer · Kisumu, Kenya 🇰🇪*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-James_Koero-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/james-koero)
[![GitHub](https://img.shields.io/badge/GitHub-jameskoero-181717?style=for-the-badge&logo=github)](https://github.com/jameskoero)
[![Email](https://img.shields.io/badge/Email-jmskoero%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:jmskoero@gmail.com)
[![Portfolio](https://img.shields.io/badge/Live_App-cmdms.onrender.com-46E3B7?style=for-the-badge&logo=render)](https://cmdms.onrender.com)

> **Hiring?** This repo is my resume.
> The code, docs, tests, and deployment pipeline speak for themselves.

</div>

---

<div align="center">

⭐ **Star this repo** if you believe in pay transparency for African tech workers

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
