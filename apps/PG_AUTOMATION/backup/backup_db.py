import subprocess
from datetime import datetime


def backup_database():

    backup_file = (
        f"/tmp/retinahalo_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.dump"
    )

    cmd = (
        f"PGPASSWORD=postgres123 "
        f"pg_dump -Fc -U postgres retinahalo "
        f"> {backup_file}"
    )

    subprocess.run(cmd, shell=True, check=True)

    print(f"Database backup created: {backup_file}")
