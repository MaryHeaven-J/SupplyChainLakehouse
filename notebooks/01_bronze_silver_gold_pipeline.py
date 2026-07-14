# STEP 1 - Create Raw Data

data = [
    (1001,"Laptop",10,50000,"India"),
    (1002,"Monitor",20,12000,"USA"),
    (1003,"Keyboard",50,1500,"India"),
    (1004,"Mouse",100,800,"UK")
]

columns = ["OrderID","Product","Quantity","Price","Country"]

df = spark.createDataFrame(data,columns)

# Bronze Layer

df.write \
.mode("overwrite") \
.saveAsTable("bronze_orders")

# Read Bronze

bronze_df = spark.sql(
"SELECT * FROM bronze_orders"
)

# Silver Layer

silver_df = bronze_df.dropDuplicates()

# Revenue Calculation

from pyspark.sql.functions import *

silver_df = silver_df.withColumn(
"Revenue",
col("Quantity") * col("Price")
)

silver_df.write \
.mode("overwrite") \
.saveAsTable("silver_orders")

# Gold Layer

gold_df = silver_df.groupBy(
"Country"
).agg(
sum("Revenue").alias("Total_Revenue")
)

gold_df.write \
.mode("overwrite") \
.saveAsTable("gold_country_revenue")

print("Pipeline Executed Successfully")
