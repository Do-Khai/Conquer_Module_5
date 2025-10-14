# feature_repo/feature_view.py
from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64
from datetime import timedelta
from advertising_data_source import advertising_source  

ad_entity = Entity(name="product", 
                   description="Product name" ,
                   join_keys=["productID"])

advertising_features = FeatureView(
    name="advertising_features",
    entities=[ad_entity],
    ttl=timedelta(days=365),
    schema=[
        Field(name="TV", dtype=Float32),
        Field(name="Radio", dtype=Float32),
        Field(name="Newspaper", dtype=Float32),
        Field(name="Sales", dtype=Float32),
    ],
    source=advertising_source,
    online=True,
)
