import logging

import psycopg2

from database.db_config import DB_CONFIG

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)


TABLES = [
    """
    CREATE TABLE IF NOT EXISTS customers (
        customer_id UUID PRIMARY KEY,
        full_name VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        phone VARCHAR(20),
        company_name VARCHAR(255),
        status VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS sites (
        site_id UUID PRIMARY KEY,
        customer_id UUID REFERENCES customers(customer_id),
        site_name VARCHAR(255),
        address TEXT,
        timezone VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS cameras (
        camera_id UUID PRIMARY KEY,
        site_id UUID REFERENCES sites(site_id),
        camera_name VARCHAR(255),
        camera_model VARCHAR(100),
        serial_number VARCHAR(100),
        stream_url TEXT,
        status VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS recordings (
        recording_id UUID PRIMARY KEY,
        camera_id UUID REFERENCES cameras(camera_id),
        s3_path TEXT,
        file_size BIGINT,
        recording_start TIMESTAMP,
        recording_end TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS ai_events (
        event_id UUID PRIMARY KEY,
        camera_id UUID REFERENCES cameras(camera_id),
        event_type VARCHAR(50),
        confidence NUMERIC(5,2),
        snapshot_path TEXT,
        clip_path TEXT,
        event_time TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id UUID PRIMARY KEY,
        customer_id UUID REFERENCES customers(customer_id),
        plan_name VARCHAR(100),
        start_date DATE,
        end_date DATE,
        status VARCHAR(20)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS storage_usage (
        usage_id UUID PRIMARY KEY,
        customer_id UUID REFERENCES customers(customer_id),
        used_storage_gb NUMERIC(10,2),
        usage_date DATE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS camera_health (
        health_id UUID PRIMARY KEY,
        camera_id UUID REFERENCES cameras(camera_id),
        online BOOLEAN,
        fps NUMERIC(5,2),
        bitrate NUMERIC(10,2),
        storage_used_gb NUMERIC(10,2),
        checked_at TIMESTAMP
    );
    """,
]

INDEXES = [
    """
    CREATE INDEX IF NOT EXISTS idx_customers_email
    ON customers(email);
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_sites_customer
    ON sites(customer_id);
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_cameras_site
    ON cameras(site_id);
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_recordings_camera
    ON recordings(camera_id);
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_ai_events_camera
    ON ai_events(camera_id);
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_storage_usage_customer
    ON storage_usage(customer_id);
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_camera_health_camera
    ON camera_health(camera_id);
    """,
]


class CreateTables:
    def __init__(self):
        self.config = DB_CONFIG

    def get_connection(self):
        return psycopg2.connect(**self.config)

    def create_tables(self):
        try:
            logger.info("Connecting to PostgreSQL database")

            with self.get_connection() as conn:
                with conn.cursor() as cur:

                    logger.info("Creating tables")

                    for table in TABLES:
                        cur.execute(table)

                    logger.info("Creating indexes")

                    for index in INDEXES:
                        cur.execute(index)

                conn.commit()

            logger.info(
                "Successfully created %s tables and %s indexes",
                len(TABLES),
                len(INDEXES),
            )

        except Exception as error:
            logger.exception("Failed to create tables: %s", error)
            raise


def create_tables():
    CreateTables().create_tables()


if __name__ == "__main__":
    create_tables()
