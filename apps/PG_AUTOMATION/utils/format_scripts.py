import subprocess
import sys


def format_scripts():

    print("Formatting Python files using Black...")

    cmd = "black ."

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)

    print(result.stdout)
    print("Formatting completed successfully.")
