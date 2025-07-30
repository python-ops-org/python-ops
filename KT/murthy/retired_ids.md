
```
import csv
import re

def extract_active_author_emails(input_file="input.csv", output_file="output.csv"):
    infile = open(input_file, "r")
    outfile = open(output_file, "w")

    reader = csv.DictReader(infile)
    fieldnames = ["book_id", "authors", "project_status", "contact_emails"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        status = row["project_status"].strip().lower()
        if status == "active":
            emails = re.split(r"[;,]", row["contact_emails"])
            for email in emails:
                email = email.strip()
                if (
                    "noreply.gitlab.com" in email or
                    email == "list@gmail.com" or
                    email == "gitlabapacsupport@gmail.com"
                ):
                    continue
                clean_row = {
                    "book_id": row["book_id"].strip(),
                    "authors": row["authors"].strip(),
                    "project_status": row["project_status"].strip(),
                    "contact_emails": email
                }
                writer.writerow(clean_row)
                # Print in CSV format
                print(f'{clean_row["book_id"]},{clean_row["authors"]},{clean_row["project_status"]},{clean_row["contact_emails"]}')
                break  # Only first valid author email

    infile.close()
    outfile.close()
    print(f"\n✅ Output also saved to: {output_file}")

# Run it
extract_active_author_emails()


```
