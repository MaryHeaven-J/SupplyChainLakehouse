# Supply Chain Lakehouse Project

## Overview

This project demonstrates an end-to-end Data Engineering solution built using Databricks, PySpark, SQL and Delta Lake.

The objective is to simulate a real-world supply chain analytics platform that ingests raw order data, performs ETL transformations, applies data quality checks and generates business KPIs using a Lakehouse architecture.

---

## Architecture

Source Data
→ Bronze Layer
→ Silver Layer
→ Gold Layer
→ SQL Analytics
→ Power BI

---

## Technologies Used

- Databricks
- PySpark
- SQL
- Delta Lake
- Python
- GitHub

---

## Medallion Architecture

### Bronze Layer
Stores raw source data.

### Silver Layer
Performs:
- Null handling
- Duplicate removal
- Data validation

### Gold Layer
Creates:
- Revenue KPIs
- Country Revenue Summary
- Inventory Status Metrics

---

## Business KPIs

### Revenue Analysis

Country-wise Revenue

### Inventory Analysis

Inventory Risk Classification

### Order Analysis

High Value Orders
Normal Orders

---
## Project Screenshots

### Bronze Layer

Raw data ingestion into the Lakehouse.

### Silver Layer

Data cleansing:
- Removed duplicates
- Removed null values
- Added revenue calculations

### Gold Layer

Business KPI layer:
- Country Revenue Analysis
- Aggregated metrics
- Reporting-ready dataset
## Future Enhancements

- Azure Data Factory
- Delta Lake Time Travel
- Change Data Capture
- Kafka Streaming
- Power BI Dashboard
- CI/CD Pipelines

---

## Author

Mary Heaven J
Data Analyst | Aspiring Data Engineer
