import argparse

from install.install import install_postgresql
from create_table.create_table import create_tables
from insert_data.insert_data import insert_data
from backup.backup_db import backup_database
from backup.backup_tables import backup_tables
from utils.format_scripts import format_scripts


class RunManager:

    @staticmethod
    def execute(action):

        actions = {
            "install_postgresql": install_postgresql,
            "create_table": create_tables,
            "insert_table": insert_data,
            "backup_db": backup_database,
            "backup_tables": backup_tables,
            "format_scripts": format_scripts,
        }

        if action not in actions:
            raise ValueError(f"Unsupported action: {action}")

        actions[action]()


def main():

    parser = argparse.ArgumentParser(
        description="RetinaHalo PostgreSQL Management Utility"
    )

    parser.add_argument(
        "--action",
        required=True,
        choices=[
            "install_postgresql",
            "create_table",
            "insert_table",
            "backup_db",
            "backup_tables",
            "format_scripts",
        ],
        help="Action to execute",
    )

    args = parser.parse_args()

    RunManager.execute(args.action)


if __name__ == "__main__":
    main()
