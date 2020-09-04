from datetime import time
import dask.dataframe as dd

time
df = dd.read_csv("/home/phani/datasets/spacemissions.csv", encoding='unicode_escape')
print(df.head())

##From HDFS

import dask

dask.config.set({"hdfs_driver": "hdfs3"})
df1 = dd.read_json("hdfs://localhost:54310/user/data/space_missions1/*.json")
print(df1.head())
