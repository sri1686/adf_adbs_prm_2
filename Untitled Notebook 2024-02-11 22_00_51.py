# Databricks notebook source
# # Mounting code
# dbutils.fs.mount(
#   source="wasbs://input@storageaccount1686.blob.core.windows.net/",
#   mount_point="/mnt/my-mount",
#   extra_configs={
#     "fs.azure.account.key.storageaccount1686.blob.core.windows.net": "7FpgEb0knKTvY/5alNx9XKeD7XIhxlAiPMgqN678qDTl0ntj8OL/uo3ZnBHzcCPQTWo4DpEQQiLA+AStFaM13Q=="
#   }
# )

# COMMAND ----------

dbutils.fs.ls("/mnt/my-mount")

# COMMAND ----------

df=spark.read.csv("dbfs:/mnt/my-mount/sample.csv")

# COMMAND ----------

# Correct usage for writing a DataFrame to a Parquet file
df.write.csv("dbfs:/mnt/my-mount/out_sample.csv")


# COMMAND ----------

df=spark.read.csv("dbfs:/mnt/my-mount/out_sample.csv")

# COMMAND ----------

df.display()

# COMMAND ----------


