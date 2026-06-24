import uuid
import psycopg2

from database.db_config import DB_CONFIG


class InsertData:

    def __init__(self):
        self.config = DB_CONFIG

    def get_connection(self):
        return psycopg2.connect(
            host=self.config["host"],
            database=self.config["database"],
            user=self.config["user"],
            password=self.config["password"],
        )

    def insert_customer(self, cur):

        self.customer_id = str(uuid.uuid4())

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
            """,
            (
                self.customer_id,
                "Sudipta Chakraborty",
                "admin@retinahalo.com",
                "9876543210",
                "RetinaHalo",
                "ACTIVE",
            ),
        )

    def insert_site(self, cur):

        self.site_id = str(uuid.uuid4())

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
                self.site_id,
                self.customer_id,
                "Kolkata Office",
                "Newtown, Kolkata",
                "Asia/Kolkata",
            ),
        )

    def insert_camera(self, cur):

        self.camera_id = str(uuid.uuid4())

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
                self.camera_id,
                self.site_id,
                "Parking Camera",
                "Hikvision DS-2CD",
                "CAM001",
                "rtsp://camera1/live",
                "ONLINE",
            ),
        )

    def insert_subscription(self, cur):

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
                self.customer_id,
                "Premium",
                "ACTIVE",
            ),
        )

    def execute(self):

        conn = None

        try:
            conn = self.get_connection()
            cur = conn.cursor()

            self.insert_customer(cur)
            self.insert_site(cur)
            self.insert_camera(cur)
            self.insert_subscription(cur)

            conn.commit()

            print("Sample RetinaHalo data inserted successfully")

        except Exception as error:
            print(f"Insert failed: {error}")

            if conn:
                conn.rollback()

            raise

        finally:
            if conn:
                cur.close()
                conn.close()


def insert_data():
    inserter = InsertData()
    inserter.execute()


if __name__ == "__main__":
    insert_data()
