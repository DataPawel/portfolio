# Overview

This capstone project, completed as part of the CAS in Data Engineering and Applied Data Science at HSLU, focuses on the development of an interactive tool for analyzing medical research trends using PubMed metadata.

The solution automates the full ETL pipeline — from data retrieval via the PubMed API, through transformation and storage in PostgreSQL, to visualization in Power BI. 

## Purpose and Usage

This project is designed to help researchers, analysts and academic professionals track and explore trends in biomedical research. Using metadata from PubMed, the tool enables users to identify topic frequency, track author contributions, or explore journal-specific trends over a selected time period. 

To use the tool:
- Open `01_Data_Fetching_and_Cleaning.ipynb` to fetch and clean data. Adjusting a list of search terms and a time window and run the file.
- Open and run `02_Database_Creation.ipynb` to create and populate the PostgreSQL database
- Visualize the data in Power BI by connecting PostgreSQL as a source.

**Note:** The Power BI dashboard was not the main focus of this project. While functional, it serves primarily as a demonstration tool. The primary focus was on building a scalable and automated data pipeline.

## Project Structure

The project is divided into modular parts to simplify development. Parts 1 and 2 can be combined to streamline execution and improve performance.
```
.
├── 01_Data_Fetching_and_Cleaning.ipynb     # Python notebook to retrieve and clean PubMed data
├── 02_Database_Creation.ipynb              # PostgreSQL schema creation and data loading script
├── 03_PowerBI_Dashboard.pbix               # Example Power BI dashboard
├── 04_Articles_Dataframe.parquet           # Cleaned example dataset in Parquet format
├── 05_Pawel_Wiezel_Capstone_Project.pdf    # Final project report (Transferarbeit)
```

## Technologies Used

- Python 3
  - requests, pandas, xml.etree.ElementTree for data extraction and transformation
- PostgreSQL
  - Snowflake schema with bridge and dimension tables
- Power BI
  - Interactive dashboard for trend analysis
- PubMed Entrez API
  - For retrieving metadata on biomedical literature
- Jupyter Notebooks
  - For structured ETL implementation

## Highlights

- Fetching speed is 3 requests per second without an API key and 10 with a key (The key can be requested here https://support.nlm.nih.gov/kbArticle/?pn=KA-05317)
- Uses ETL best practices, normalized schema, and interactive analytics

## Copyright

Developed and owned by Pawel Wiezel as a final Transferarbeit for the CAS in Data Engineering and Applied Data Science at Hochschule Luzern (HSLU).
