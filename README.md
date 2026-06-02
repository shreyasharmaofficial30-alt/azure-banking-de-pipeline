# Project Overview 🏦 

Built an end-to-end Azure Data Engineering solution for banking customer data processing. The pipeline ingests historical and newly arrived customer files using Azure Data Factory, stores data in Azure Data Lake Storage Gen2, performs transformations in Azure Databricks, and writes the processed output in Delta format.

The solution demonstrates bulk and scheduled file-based incremental ingestion, secure authentication using Service Principals, and data transformation workflows to generate analytics-ready datasets for reporting and business consumption.

# Client Requirement
Build an end-to-end Azure Data Engineering solution to process customer data from 2010–2025. The platform should support large-scale historical data ingestion, automated processing of newly arriving data, and identify premium customers with a credit score greater than 800.

# Architecture
```text
┌─────────────────────────────────────────────┐
│                 Source Layer                │
├─────────────────────────────────────────────┤
│ CSV Files │ SFTP │ SharePoint │ Blob Storage│
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│        Azure Data Factory (ADF)             │
├─────────────────────────────────────────────┤
│ Copy Activity                              │
│ CSV → Parquet Conversion                   │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│        ADLS Gen2 - Storage Account 1        │
├─────────────────────────────────────────────┤
│ Bronze Layer (inputcontainer)              │
│ Raw Parquet Files                          │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│     Azure Databricks (Serverless)           │
├─────────────────────────────────────────────┤
│ PySpark Transformations                    │
│ Customer Filtering                         │
│ Data Processing                            │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│      Service Principal (OAuth)              │
├─────────────────────────────────────────────┤
│ Secure Authentication & Authorization      │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│        ADLS Gen2 - Storage Account 2        │
├─────────────────────────────────────────────┤
│ Silver Layer (output container)            │
│ Delta Format Storage                       │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│             Power BI (Planned)              │
├─────────────────────────────────────────────┤
│ Dashboards & Reporting                     │
└─────────────────────────────────────────────┘
```
# Azure Services Used

✅ Azure Data Factory (ADF)
- Data ingestion
- CSV → Parquet conversion
- Scheduled pipeline execution

✅ Azure Data Lake Storage Gen2 (Storage Account 1)
- Bronze layer
- Raw Parquet storage

✅ Azure Data Lake Storage Gen2 (Storage Account 2)
- Silver layer
- Delta format storage

✅ Azure Databricks (Serverless)
- PySpark transformations
- Business rule implementation

✅ Azure App Registration
- Service Principal authentication

✅ Azure IAM
- Role-based access control (RBAC)

✅ Storage Account Access Keys
- Secure connectivity between Azure services

## Medallion Architecture

### Bronze Layer
- Customer CSV files uploaded to the landing container.
- Azure Data Factory ingests the files and converts them into Parquet format.
- Raw data is stored in ADLS Gen2.

### Silver Layer
- Azure Databricks reads the Bronze data.
- Business transformations are applied using PySpark.
- Premium customers with credit score > 800 are identified.
- Processed data is stored in Delta format.

### Gold Layer
- Aggregated business KPI dataset created from the Silver layer.
- Total Premium Customers metric is calculated.
- Stored in Delta format for reporting and analytics consumption.

## Dataset
- **Dataset Name:** Financial Transactions Dataset: Analytics
- **Source:** Kaggle
- **Dataset Link:** https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets

## Challenges & Solutions

| Challenge                                        | Solution                                   |
| ------------------------------------------------ | ------------------------------------------ |
| Azure Student Subscription region restrictions   | Used Southeast Asia region                 |
| `dbutils.fs.mount()` not supported on Serverless | Used OAuth authentication with `.option()` |
| ADF–Databricks Linked Service Error (9512)       | Used Databricks Jobs for execution         |
| Globally unique resource name requirement        | Added unique suffixes to resource names    |
| Secure Databricks access to ADLS                 | Configured Service Principal and IAM roles |

## Planned Improvements

- Replace hardcoded secrets with Azure Key Vault
- Connect Power BI for reporting and dashboarding
- Implement true incremental loading using watermarking or Delta MERGE
- Add additional business KPIs and metrics in the Gold layer

## Why This Project Matters

* Demonstrates how historical customer data can be ingested and processed at scale using Azure services.
* Implements a common cloud-to-cloud ingestion pattern used in enterprise data platforms.
* Shows how Azure Data Factory can automate data ingestion through scheduled pipeline execution.
* Demonstrates conversion of raw CSV files into optimized Parquet format for analytics workloads.
* Implements secure access between Databricks and ADLS using Service Principal authentication and IAM roles.
* Applies the Medallion Architecture (Bronze → Silver → Gold) for data organization and governance.
* Uses Delta Lake to store curated datasets and business KPIs.
* Simulates a real-world banking use case by identifying premium customers based on business rules.

## Tech Stack
Azure Data Factory · ADLS Gen2 · Azure Databricks · Delta Lake · PySpark · Python · Azure App Registration 

