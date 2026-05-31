# Databricks notebook source
# Read file 1 (what you see now)
client_id = ""
tenant_id = ""
client_secret = ""
storage_account = ""
container = ""

df1 = (spark.read.format("parquet")
  .option("fs.azure.account.auth.type.adlsdevbankdomainp1.dfs.core.windows.net", "OAuth")
  .option("fs.azure.account.oauth.provider.type.adlsdevbankdomainp1.dfs.core.windows.net", 
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
  .option("fs.azure.account.oauth2.client.id.adlsdevbankdomainp1.dfs.core.windows.net", 
    client_id)
  .option("fs.azure.account.oauth2.client.secret.adlsdevbankdomainp1.dfs.core.windows.net", 
    client_secret)
  .option("fs.azure.account.oauth2.client.endpoint.adlsdevbankdomainp1.dfs.core.windows.net",
    f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")
  .load("abfss://container_name@storage_account_name.dfs.core.windows.net/file_name.parquet")
)
df1.display()


# COMMAND ----------

from pyspark.sql.functions import col

filtered_df = df1.filter(col("credit_score") > 800)\
                .select("id","credit_Score")

filtered_df.display()                


# COMMAND ----------

# MAGIC %md
# MAGIC store the filtered data in final storage account adls gen2

# COMMAND ----------

(filtered_df.write
  .format("delta")
  .mode("overwrite")
  .option("overwriteSchema", "true")
  .option("fs.azure.account.auth.type.adlsdevbankdomainp2.dfs.core.windows.net", "OAuth")
  .option("fs.azure.account.oauth.provider.type.adlsdevbankdomainp2.dfs.core.windows.net", 
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
  .option("fs.azure.account.oauth2.client.id.adlsdevbankdomainp2.dfs.core.windows.net", 
    client_id)
  .option("fs.azure.account.oauth2.client.secret.adlsdevbankdomainp2.dfs.core.windows.net", 
    client_secret)
  .option("fs.azure.account.oauth2.client.endpoint.adlsdevbankdomainp2.dfs.core.windows.net",
    f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")
  .save("abfss://output@storage_account_name.dfs.core.windows.net/newfilename")
)

# COMMAND ----------

# MAGIC %md
# MAGIC add a gold layer where u store total premium customers

# COMMAND ----------

from pyspark.sql.functions import count

gold_df = filtered_df.agg(
    count("*").alias("total_premium_customers")
)

gold_df.display()