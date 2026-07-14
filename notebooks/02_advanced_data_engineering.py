# Advanced Data Engineering Concepts
# Project: Supply Chain Lakehouse
# Tools: Databricks, PySpark, SQL

from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.sql.functions import broadcast

# -----------------------------------------
# STEP 1: Create Orders Data
# -----------------------------------------

orders_data = [
    (1001, "Laptop", 10, 50000, "India"),
    (1002, "Monitor", 20, 12000, "USA"),
    (1003, "Keyboard", 50, 1500, "India"),
    (1004, "Mouse", 100, 800, "UK"),
    (1005, "Laptop", 5, 50000, "Germany"),
    (1006, "Monitor", 15, 12000, "Canada"),
    (1007, "Keyboard", 30, 1500, "Singapore"),
    (1008, "Mouse", 200, 800, "India")
]

orders_columns = [
    "OrderID",
    "Product",
    "Quantity",
    "Price",
    "Country"
]

orders_df = spark.createDataFrame(
    orders_data,
    orders_columns
)

orders_df = orders_df.withColumn(
    "Revenue",
    col("Quantity") * col("Price")
)

display(orders_df)


# -----------------------------------------
# STEP 2: Create Inventory Data
# -----------------------------------------

inventory_data = [
    ("Laptop", 500),
    ("Monitor", 50),
    ("Keyboard", 100),
    ("Mouse", 20)
]

inventory_columns = [
    "Product",
    "Inventory"
]

inventory_df = spark.createDataFrame(
    inventory_data,
    inventory_columns
)

display(inventory_df)


# -----------------------------------------
# STEP 3: Spark Join
# -----------------------------------------

# Joining Orders with Inventory using Product column

joined_df = orders_df.join(
    inventory_df,
    on="Product",
    how="left"
)

display(joined_df)


# -----------------------------------------
# STEP 4: Inventory Risk Classification
# -----------------------------------------

inventory_risk_df = joined_df.withColumn(
    "Inventory_Status",
    when(col("Inventory") < 50, "Critical")
    .when(col("Inventory") < 100, "Low")
    .otherwise("Healthy")
)

display(inventory_risk_df)


# -----------------------------------------
# STEP 5: Window Function - Revenue Ranking by Country
# -----------------------------------------

window_spec = Window.partitionBy(
    "Country"
).orderBy(
    col("Revenue").desc()
)

ranked_orders_df = inventory_risk_df.withColumn(
    "Revenue_Rank",
    row_number().over(window_spec)
)

display(ranked_orders_df)


# -----------------------------------------
# STEP 6: Country Level KPI Aggregation
# -----------------------------------------

country_kpi_df = ranked_orders_df.groupBy(
    "Country"
).agg(
    sum("Revenue").alias("Total_Revenue"),
    count("OrderID").alias("Total_Orders"),
    avg("Revenue").alias("Average_Order_Value")
)

display(country_kpi_df)


# -----------------------------------------
# STEP 7: Save Advanced Gold Table
# -----------------------------------------

country_kpi_df.write \
.mode("overwrite") \
.saveAsTable("gold_country_kpi")

print("Advanced Gold KPI Table Created Successfully")


# -----------------------------------------
# STEP 8: Broadcast Join Concept
# -----------------------------------------

# Broadcast join is used when one table is small.
# Here inventory_df is small, so Spark can broadcast it to all worker nodes.

broadcast_join_df = orders_df.join(
    broadcast(inventory_df),
    on="Product",
    how="left"
)

display(broadcast_join_df)


# -----------------------------------------
# STEP 9: Cache Concept
# -----------------------------------------

# Caching stores frequently used DataFrame in memory.
# It improves performance when the same DataFrame is used multiple times.

ranked_orders_df.cache()

print("Advanced Data Engineering Notebook Executed Successfully")
``
