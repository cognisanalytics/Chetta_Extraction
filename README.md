# SQL Server → PostgreSQL (dlt pipeline)

Replicates all tables from a SQL Server database into PostgreSQL using [dlt](https://dlthub.com/).

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed

## Setup

```bash
# Install dependencies (automatically fetches Python 3.10 if needed)
uv sync

# Configure credentials
cp .dlt/secrets.example.copy.toml .dlt/secrets.toml
# Then edit .dlt/secrets.toml with your SQL Server and PostgreSQL credentials
```

## Run

```bash
uv run python main.py
```

