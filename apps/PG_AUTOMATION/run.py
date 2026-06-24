import argparse
import logging
import sys

from backup.backup_db import backup_database
from backup.backup_tables import backup_tables
from create_table.create_table import create_tables
from insert_data.insert_data import insert_data
from install.install import install_postgresql
from utils.format_scripts import format_scripts

VERSION = "1.0.0"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)

ACTIONS = {
    "install_postgresql": install_postgresql,
    "create_table": create_tables,
    "insert_table": insert_data,
    "backup_db": backup_database,
    "backup_tables": backup_tables,
    "format_scripts": format_scripts,
}


class RunManager:

    @staticmethod
    def execute(action):

        logger.info("Executing action: %s", action)

        try:
            ACTIONS[action]()
            logger.info("Action completed successfully")

        except Exception as error:
            logger.exception(
                "Action '%s' failed: %s",
                action,
                error,
            )
            sys.exit(1)


def main():

    parser = argparse.ArgumentParser(
        description="RetinaHalo PostgreSQL Management Utility",
        epilog="""
Examples:

python run.py --action install_postgresql

python run.py --action create_table

python run.py --action insert_table

python run.py --action backup_db

python run.py --action backup_tables

python run.py --action format_scripts

python run.py --version
""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--action",
        choices=ACTIONS.keys(),
        help="Action to execute",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Display utility version",
    )

    args = parser.parse_args()

    if args.version:
        print(f"RetinaHalo PostgreSQL Utility v{VERSION}")
        sys.exit(0)

    if not args.action:
        parser.print_help()
        sys.exit(1)

    RunManager.execute(args.action)


if __name__ == "__main__":
    main()
