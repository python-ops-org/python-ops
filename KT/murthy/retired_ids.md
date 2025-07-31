
```
import csv
import re

def extract_valid_author_emails(input_file="input.csv", output_file="output.csv"):
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ["book_id", "project_status", "contact_emails"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            status = row["project_status"].strip().lower()
            if status == "active":
                emails = re.split(r"[;,]", row["contact_emails"])
                valid_emails = [
                    email.strip()
                    for email in emails
                    if not (
                        "noreply.gitlab.com" in email
                        or email.strip() == "list@gmail.com"
                        or email.strip() == "gitlabapacsupport@gmail.com"
                    )
                ]
                if valid_emails:
                    clean_row = {
                        "book_id": row["book_id"].strip(),
                        "project_status": row["project_status"].strip(),
                        "contact_emails": ",".join(valid_emails)
                    }
                    writer.writerow(clean_row)
                    print(f'{clean_row["book_id"]},{clean_row["project_status"]},{clean_row["contact_emails"]}')

    print(f"\n✅ Output also saved to: {output_file}")

# Run the function
extract_valid_author_emails()


```
