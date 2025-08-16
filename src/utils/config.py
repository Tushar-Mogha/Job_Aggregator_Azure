# src/utils/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ----------------------------
# Scraping Configs (Internshala)
# ----------------------------

INTERN_SHALA_BASE_URL = "https://internshala.com/"  # public listings
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ----------------------------
# Azure Blob Storage Configs
# ----------------------------
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "job4all_data")

# ----------------------------
# Optional: Azure SQL / Cosmos DB (Free Tier)
# ----------------------------
AZURE_SQL_CONN_STRING = os.getenv("AZURE_SQL_CONN_STRING", "")
AZURE_SQL_DB_NAME = os.getenv("AZURE_SQL_DB_NAME", "JobAggregatorDB")