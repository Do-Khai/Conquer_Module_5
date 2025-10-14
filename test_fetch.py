from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="feature_repo")

entity_df = pd.DataFrame({
    "productID": [1,2,3],
    "event_timestamp": pd.to_datetime([pd.Timestamp.now()] * 3)
})

df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "advertising_features:TV",
        "advertising_features:Radio",
        "advertising_features:Newspaper",
        "advertising_features:Sales",
    ]
).to_df()

print(df.head())
