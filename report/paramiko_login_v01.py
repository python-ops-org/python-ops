import subprocess
import re
import argparse
import csv
from datetime import datetime

def main(inventory_path, playbook_path, output_csv):
    # Run the Ansible playbook and capture the output

    start_time = datetime.now()
    print(f"Script started at: {start_time}")

    playbook_command = f"ansible-playbook -i {inventory_path} {playbook_path}"
    result = subprocess.run(playbook_command, shell=True, stdout=subprocess.PIPE, text=True)

    # Get the stdout of the playbook execution
    playbook_output = result.stdout

    # Extract IP address, memory usage, and CPU usage using regular expressions
    ip_address_matches = re.findall(r'"ansible_default_ipv4\.address": "(.*?)"', playbook_output)
    memory_usage_matches = re.findall(r'"msg": "([0-9]+)"', playbook_output)
    cpu_usage_matches = re.findall(r'"msg": "([0-9.]+%)"', playbook_output)


    # Check if matches were found and store the values in separate lists
    ip_addresses = []
    memory_usage = []
    cpu_usage = []

    if ip_address_matches:
        ip_addresses.extend(ip_address_matches)

    if memory_usage_matches:
        memory_usage.extend(memory_usage_matches)

    if cpu_usage_matches:
        cpu_usage.extend(cpu_usage_matches)

    # Print the header
    print("IP_Address\tMemory_Usage\tCPU_Usage")

    # Write data to CSV file
    with open(output_csv, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["IP_Address", "Memory_Usage", "CPU_Usage"])

        # Iterate over the lists and print and write the data
        for ip, mem, cpu in zip(ip_addresses, memory_usage, cpu_usage):
            output = f"{ip}\t{mem}\t\t{cpu}"
            print(output)
            #print(f"{ip}\t{mem}\t\t{cpu}")
            csv_writer.writerow([ip, mem, cpu])

    end_time = datetime.now()
    print(f"Script ended at: {end_time}")
    print(f"Data written to {output_csv}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract data from Ansible playbook and print in the desired format and write to CSV")
    parser.add_argument("-i", "--inventory", required=True, help="Path to the Ansible inventory")
    parser.add_argument("-p", "--playbook", required=True, help="Path to the Ansible playbook")
    parser.add_argument("-o", "--output", required=True, help="Path to the output CSV file")
    args = parser.parse_args()
    main(args.inventory, args.playbook, args.output)

(base) root@controller:/home/nik/Desktop/git_ops/ansible# cat paramiko_login.py 
import paramiko
import argparse


def ssh_execute_command(hostname, username, command):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()

        # Automatically add host keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host
        client.connect(hostname, username=username)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Read the output
        output = stdout.read().decode("utf-8")

        # Close the SSH connection
        client.close()

        return output.strip()  # Strip leading/trailing whitespaces
    except Exception as e:
        return str(e)


def read_inventory(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    hosts = []
    for line in lines:
        if line.startswith("#") or not line.strip():
            continue

        parts = line.strip().split()
        if len(parts) == 3:
            host = {
                "name": parts[0],
                "hostname": parts[1].split("=")[1],
                "username": parts[2].split("=")[1],
            }
            hosts.append(host)

    return hosts


memory_command = "free -m | sed -n '2p' | awk '{print $3;}'"
cpu_command = (
    "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1\"%\"}'"
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch memory and CPU usage from remote hosts")
    parser.add_argument("-i", "--inventory", required=True, help="Path to the Ansible inventory file")
    args = parser.parse_args()

    # Read host and login details from the inventory file
    inventory_path = args.inventory
    hosts = read_inventory(inventory_path)

    # Print the header
    print("Host\t\tMemory_Usage\tCPU_Usage")

    # Iterate through the hosts and fetch memory and CPU usage
    for host in hosts:
        memory_output = ssh_execute_command(host["hostname"], host["username"], memory_command)
        cpu_output = ssh_execute_command(host["hostname"], host["username"], cpu_command)

        # Format the output
        output = f"{host['hostname']}\t{memory_output}\t\t{cpu_output}"

        # Print the output
        print(output)
