# src/prepare_feast_data.py
import pandas as pd
import os
from datetime import datetime, timedelta

def prepare_advertising_csv(src_csv="data/advertising.csv",
                            out_parquet=os.path.join("feature_repo", "data_processed", "advertising.parquet")):
    os.makedirs(os.path.dirname(out_parquet), exist_ok=True)
    df = pd.read_csv(src_csv)

    # nếu đã có cột productID/event_timestamp thì bỏ qua bước tạo
    if "productID" not in df.columns:
        df.insert(0, "productID", range(1, len(df) + 1))  # 1-based id

    if "event_timestamp" not in df.columns:
        # tạo timestamp giả lập: dùng ngày hiện tại - i seconds để có thứ tự
        now = datetime.utcnow()
        df["event_timestamp"] = [now - timedelta(seconds=i) for i in range(len(df))]

    # lưu parquet (Feast thích parquet)
    df.to_parquet(out_parquet, index=False)
    print(f"Saved parquet to: {out_parquet}")

if __name__ == "__main__":
    prepare_advertising_csv()
