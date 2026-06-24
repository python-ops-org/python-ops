import psycopg2
from database.db_config import DB_CONFIG


class CreateTables:

    def __init__(
        self,
        host="localhost",
        database="retinahalo",
        user="postgres",
        password="postgres123"
    ):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def get_tables(self):
        return [

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
            """
        ]

    def create_tables(self):

        conn = None

        try:
            conn = self.get_connection()
            cur = conn.cursor()

            for table in self.get_tables():
                cur.execute(table)

            conn.commit()

            print("RetinaHalo tables created successfully")

        except Exception as error:
            print(f"Error creating tables: {error}")
            raise

        finally:
            if conn:
                cur.close()
                conn.close()


def create_tables():
    creator = CreateTables()
    creator.create_tables()


if __name__ == "__main__":
    create_tables()
