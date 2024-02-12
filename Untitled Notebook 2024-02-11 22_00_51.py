# Databricks notebook source
# Mounting code
dbutils.fs.mount(
  source="wasbs://input@storageaccount1686.blob.core.windows.net/",
  mount_point="/mnt/my-mount",
  extra_configs={
    "fs.azure.account.key.storageaccount1686.blob.core.windows.net": "7FpgEb0knKTvY/5alNx9XKeD7XIhxlAiPMgqN678qDTl0ntj8OL/uo3ZnBHzcCPQTWo4DpEQQiLA+AStFaM13Q=="
  }
)

# COMMAND ----------

dbutils.fs.ls("/mnt/my-mount")


# COMMAND ----------


