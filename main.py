import logging

import dlt
from dlt.sources.sql_database import sql_database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    # Credentials auto-injected from .dlt/secrets.toml
    source = sql_database(backend="pyarrow")

    pipeline = dlt.pipeline(
        pipeline_name="chetta_mssql_to_pg",
        dataset_name="chetta",
        destination="postgres",
        progress="log",
    )

    load_info = pipeline.run(source, write_disposition="replace")
    logger.info("Load info: %s", load_info)


if __name__ == "__main__":
    main()