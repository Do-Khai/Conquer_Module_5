# 🧮 Linear Regression (Vectorized) with DVC

Dự án này minh họa quy trình huấn luyện mô hình **Linear Regression** sử dụng **Batch Gradient Descent (Vectorized)**,  
được quản lý toàn bộ bằng **DVC (Data Version Control)** nhằm đảm bảo khả năng *tái tạo, theo dõi và quản lý dữ liệu + mô hình*.

---

## 🚀 Mục tiêu

> Xây dựng pipeline tự động hóa từ bước **Data Preparation → Model Training → Model Tracking**  
> Giúp bất kỳ ai clone repo đều có thể **reproduce** toàn bộ kết quả chỉ bằng 1 lệnh `dvc repro`.

---

## ⚙️ Cài đặt môi trường
🧩 Yêu cầu:

Python ≥ 3.9



## 🔧 Cài đặt:
```bash
# Clone project
git clone https://github.com/Do-Khai/LR_Vectorization.git
cd LR_Vectorization

# Cài dependencies
pip install -r requirements.txt

```

## 🧭 Luồng hoạt động DVC (Data Version Control Flow)
```
        ┌────────────────────────┐
        │     advertising.csv    │
        └────────────┬───────────┘
                     │
          [ prepare stage: data_prep.py ]
                     │
     ┌───────────────▼────────────────┐
     │     x_train.npy, y_train.npy   │
     └───────────────┬────────────────┘
                     │
           [ train stage: train.py ]
                     │
     ┌───────────────▼────────────────┐
     │   model.npy, metrics.json      │
     └────────────────────────────────┘

```

## 🧠 Tham số huấn luyện
Được lưu trong file `params.yaml`:
```
train:
  epochs: 50
  learning_rate: 0.00001
model:
  type: linear_regression

```

## 📊 Kết quả huấn luyện
File `models/metrics_v1.json` chứa thông tin mô hình:
```
{
  "dataset_size": 160,
  "dataset_version": "v1",
  "model": "model_v1",
  "parameters": {
    "epochs": 50,
    "learning_rate": 0.00001
  }
}

```
