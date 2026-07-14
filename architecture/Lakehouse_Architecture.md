# Supply Chain Lakehouse Architecture

## Project Overview

This project demonstrates an end-to-end Data Engineering pipeline for a supply chain analytics use case.

The main objective is to process raw order data, clean and transform it using PySpark, and create business-ready analytical datasets using the Bronze, Silver and Gold Lakehouse architecture.

---

## Architecture Flow

Source Data
→ Bronze Layer
→ Silver Layer
→ Gold Layer
→ SQL Analytics
→ Power BI / Business Reporting

---

## 1. Source Data

The source data represents supply chain order information.

Example fields:

- OrderID
- Product
- Quantity
- Price
- Country

In a real-world enterprise environment, this data can come from:

- ERP systems
- SAP
- Excel files
- APIs
- Databases
- Cloud storage

---

## 2. Bronze Layer

The Bronze Layer stores raw data as received from the source.

### Purpose

- Preserve original source data
- Maintain raw historical records
- Support reprocessing when business logic changes

### Table Created

```text
bronze_orders
