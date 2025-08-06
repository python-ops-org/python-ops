
```
import csv

def extract_unique_emails(input_file="output2.csv", output_file="output.csv"):
    unique_active_projects = {}

    # Exact emails to skip
    skip_exact_emails = {
        "gitlabapacsupport@credit-suisse.com",
        "gitlabnotification@credit-suisse.com",
        "notifications@credit-suisse.com",
        "gitlabadmin@credit-suisse.com",
        "noreply.gitlab.com"
    }

    # Wildcard keywords: skip if these words appear anywhere in the email
    skip_keywords = {"group", "bot", "list"}

    with open(input_file, "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if row["project_status"].strip().lower() != "active":
                continue

            project_id = row["project_id"].strip()
            cati = row["cati"].strip()
            contact_emails = row["contact_emails"].strip().strip(',')

            if not project_id or not contact_emails:
                continue

            if project_id not in unique_active_projects:
                unique_active_projects[project_id] = {
                    "cati": cati,
                    "emails": set()
                }

            # Split emails on comma or semicolon
            split_emails = contact_emails.replace(";", ",").split(",")

            for email in split_emails:
                email = email.strip().lstrip('.')  # Remove leading dot
                if (
                    email and "@" in email and ".com" in email
                    and email not in skip_exact_emails
                    and not any(keyword in email.lower() for keyword in skip_keywords)
                ):
                    unique_active_projects[project_id]["emails"].add(email)

    with open(output_file, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["cati", "project_id", "contact_emails"])
        print("cati,project_id,contact_emails")

        for project_id, data in unique_active_projects.items():
            email_list = sorted(data["emails"])
            row = [data["cati"], project_id, ",".join(email_list)]
            writer.writerow(row)
            print(",".join(row))

    print(f"\n✅ Output saved to: {output_file}")

# Run the function
extract_unique_emails()


```
