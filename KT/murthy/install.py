
import subprocess
import sys


def run(cmd):
    print(f"\nRunning: {cmd}")

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)

    print(result.stdout)


def install_postgresql():
    commands = [
        # System update
        "dnf update -y",
        # Python & Pip
        "dnf install -y tree python3 python3-pip",
         
        "wget https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/11.14.1/flyway-commandline-11.14.1-linux-x64.tar.gz",
        "tar -xzf flyway-commandline-11.14.1-linux-x64.tar.gz",
        "mv flyway-11.14.1 /opt/flyway",
        "ln -sf /opt/flyway/flyway /usr/local/bin/flyway",
        "flyway -v"



        ## UNINSTALL PG
        # "dnf remove -y postgresql15 postgresql15-server postgresql-devel"
        # PostgreSQL
        "dnf install -y postgresql15 postgresql15-server gcc python3-devel postgresql-devel",
        # Python Packages
        "pip3 install psycopg2==2.9.12",
        "pip3 install black",
        "pip3 install yamllint",
        # Docker
        "dnf install -y docker",
        # Start Docker
        "systemctl enable docker",
        "systemctl start docker",
        # Add current user to docker group
        "usermod -aG docker $USER",
        # Enable PostgreSQL
        "systemctl enable postgresql",
        "systemctl start postgresql",
        "mkdir -p /var/lib/pgsql/data"
        "chown -R postgres:postgres /var/lib/pgsql"
        "runuser -u postgres -- initdb -D /var/lib/pgsql/data",
    ]

    for cmd in commands:
        run(cmd)

    print("\nInstallation completed successfully.")


if __name__ == "__main__":
    install_postgresql()
