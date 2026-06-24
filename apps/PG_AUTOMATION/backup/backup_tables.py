import subprocess
from datetime import datetime


TABLES = [
    "customers",
    "sites",
    "cameras",
    "recordings",
    "ai_events",
    "billing",
    "subscriptions",
    "storage_plans",
    "audit_logs",
    "storage_usage",
    "device_inventory",
    "camera_health",
    "payment_transactions",
    "notifications"
]


def backup_tables():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for table in TABLES:

        backup_file = f"/tmp/{table}_{timestamp}.sql"

        cmd = (
            f"PGPASSWORD=postgres123 "
            f"pg_dump -U postgres "
            f"-t {table} "
            f"retinahalo "
            f"> {backup_file}"
        )

        subprocess.run(cmd, shell=True, check=True)

        print(f"Backed up {table} -> {backup_file}")
