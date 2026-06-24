import subprocess
import sys


def run(cmd):
    print(f"\nRunning: {cmd}")

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


def install_postgresql():
    commands = [

        # System update
        "sudo dnf update -y",

        # Python & Pip
        "sudo dnf install -y python3 python3-pip",

        # Docker
        "sudo dnf install -y docker",

        # Start Docker
        "sudo systemctl enable docker",
        "sudo systemctl start docker",

        # Add current user to docker group
        "sudo usermod -aG docker $USER",


        # PostgreSQL
        "sudo dnf install -y postgresql15 postgresql15-server",

        # Initialize PostgreSQL
        "sudo postgresql-setup --initdb",

        # Enable PostgreSQL
        "sudo systemctl enable postgresql",
        "sudo systemctl start postgresql",

        # PostgreSQL Password
        "sudo -u postgres psql -c \"ALTER USER postgres PASSWORD 'postgres123';\"",

        # Database Creation
        "sudo -u postgres createdb retinahalo",

        # Python Packages
        "pip3 install --upgrade pip",
        "pip3 install psycopg2-binary",
        "pip3 install black",
        "pip3 install yamllint"
    ]

    for cmd in commands:
        run(cmd)

    print("\nInstallation completed successfully.")


if __name__ == "__main__":
    install_postgresql()
