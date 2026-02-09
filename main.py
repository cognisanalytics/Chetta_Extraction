import logging
import os

import dlt
from dlt.sources.sql_database import sql_database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    source = sql_database()

    pipeline = dlt.pipeline(
        pipeline_name="pg_to_sqlite",
        dataset_name="chetta",
        destination="duckdb",
        progress="log",
        chunk_size=10000,
    )

    load_info = pipeline.run(source)
    logger.info("Load info: %s", load_info, write_disposition="replace")


if __name__ == "__main__":
    main()