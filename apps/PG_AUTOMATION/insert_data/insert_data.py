import logging
import uuid

import psycopg2

from database.db_config import DB_CONFIG

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)


class InsertData:

    def __init__(self):
        self.config = DB_CONFIG

    def get_connection(self):
        return psycopg2.connect(**self.config)

    def insert_customer(self, cur):

        customer_id = str(uuid.uuid4())

        cur.execute(
            """
            INSERT INTO customers (
                customer_id,
                full_name,
                email,
                phone,
                company_name,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (email) DO NOTHING
            """,
            (
                customer_id,
                "Sudipta Chakraborty",
                "admin@retinahalo.com",
                "9876543210",
                "RetinaHalo",
                "ACTIVE",
            ),
        )

        logger.info("Customer inserted")

        return customer_id

    def insert_site(self, cur, customer_id):

        site_id = str(uuid.uuid4())

        cur.execute(
            """
            INSERT INTO sites (
                site_id,
                customer_id,
                site_name,
                address,
                timezone
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                site_id,
                customer_id,
                "Kolkata Office",
                "Newtown, Kolkata",
                "Asia/Kolkata",
            ),
        )

        logger.info("Site inserted")

        return site_id

    def insert_camera(self, cur, site_id):

        camera_id = str(uuid.uuid4())

        cur.execute(
            """
            INSERT INTO cameras (
                camera_id,
                site_id,
                camera_name,
                camera_model,
                serial_number,
                stream_url,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                camera_id,
                site_id,
                "Parking Camera",
                "Hikvision DS-2CD",
                "CAM001",
                "rtsp://camera1/live",
                "ONLINE",
            ),
        )

        logger.info("Camera inserted")

        return camera_id

    def insert_subscription(self, cur, customer_id):

        subscription_id = str(uuid.uuid4())

        cur.execute(
            """
            INSERT INTO subscriptions (
                subscription_id,
                customer_id,
                plan_name,
                start_date,
                end_date,
                status
            )
            VALUES (
                %s,
                %s,
                %s,
                CURRENT_DATE,
                CURRENT_DATE + INTERVAL '30 day',
                %s
            )
            """,
            (
                subscription_id,
                customer_id,
                "Premium",
                "ACTIVE",
            ),
        )

        logger.info("Subscription inserted")

        return subscription_id

    def insert_storage_usage(self, cur, customer_id):

        usage_id = str(uuid.uuid4())

        cur.execute(
            """
            INSERT INTO storage_usage (
                usage_id,
                customer_id,
                used_storage_gb,
                usage_date
            )
            VALUES (%s, %s, %s, CURRENT_DATE)
            """,
            (
                usage_id,
                customer_id,
                25.50,
            ),
        )

        logger.info("Storage usage inserted")

    def insert_camera_health(self, cur, camera_id):

        health_id = str(uuid.uuid4())

        cur.execute(
            """
            INSERT INTO camera_health (
                health_id,
                camera_id,
                online,
                fps,
                bitrate,
                storage_used_gb,
                checked_at
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                CURRENT_TIMESTAMP
            )
            """,
            (
                health_id,
                camera_id,
                True,
                25.0,
                2048.0,
                12.5,
            ),
        )

        logger.info("Camera health inserted")

    def execute(self):

        try:

            logger.info("Connecting to PostgreSQL")

            with self.get_connection() as conn:
                with conn.cursor() as cur:

                    customer_id = self.insert_customer(cur)

                    site_id = self.insert_site(
                        cur,
                        customer_id,
                    )

                    camera_id = self.insert_camera(
                        cur,
                        site_id,
                    )

                    self.insert_subscription(
                        cur,
                        customer_id,
                    )

                    self.insert_storage_usage(
                        cur,
                        customer_id,
                    )

                    self.insert_camera_health(
                        cur,
                        camera_id,
                    )

                conn.commit()

            logger.info(
                "Sample RetinaHalo data inserted successfully"
            )

        except Exception as error:
            logger.exception(
                "Failed to insert sample data: %s",
                error,
            )
            raise


def insert_data():
    InsertData().execute()


if __name__ == "__main__":
    insert_data()
