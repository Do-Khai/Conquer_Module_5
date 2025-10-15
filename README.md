# 📊 Linear Regression with DVC & Feast

## 🧠 Overview

This project demonstrates a **complete ML pipeline** combining:

- **Machine Learning (Linear Regression)**
- **Data Versioning with DVC**
- **Feature Store Management using Feast**

It aims to provide a clear example of how to:
1. Version control your ML data and experiments.
2. Manage, materialize, and serve features consistently.
3. Build a reproducible and production-ready ML workflow.

---
## 📋 Prerequisites


Python 3.8+

Git


---
## 🚀 Quick Start

```bash
conda create -n dvc python=3.11 -y
conda activate dvc
pip install -r requirements.txt
```

```bash
# Clone the repository
https://github.com/Do-Khai/Conquer_Module_5.git
cd Conquer_Module_5

# Install dependencies
pip install -r requirements.txt
```

---
## 🤖 Basic Pipeline 
```scss
advertising.csv
   ↓
prepare_feast_data.py (generate parquet)
   ↓
Feast (apply + materialize)
   ↓
data_prep.py (split train/test)
   ↓
train.py (train model)
```
## 🚀 Production Considerations
To adapt this demo for production:

- Scalability: Use Spark for large datasets.
- Orchestration: Integrate Apache Airflow or Prefect for pipeline management.
- Monitoring: Use MLflow for experiment tracking and Prometheus for metrics.
- CI/CD: Implement automated testing and deployment pipelines.

