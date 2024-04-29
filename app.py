import polars as pl
from datetime import datetime

df = pl.DataFrame({
    "name": ["Dibimbing MSIB 6"], 
    "time": [datetime.now()]
})

print(df)