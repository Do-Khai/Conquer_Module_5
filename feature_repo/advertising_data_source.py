# feature_repo/advertising_data_source.py
import os
from feast import FileSource

HERE = os.path.dirname(__file__)
PARQUET_PATH = os.path.join(HERE, "data_processed", "advertising.parquet")

advertising_source = FileSource(
    path=PARQUET_PATH,
    event_timestamp_column="event_timestamp",
)
