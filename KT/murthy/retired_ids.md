
```
import csv
import re

def extract_author_emails(input_file="books.csv", output_file="output.csv"):
    infile = open(input_file, "r")
    outfile = open(output_file, "w")

    reader = csv.DictReader(infile)
    fieldnames = ["book_id", "status", "contact_emails"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        status = row["status"].strip().lower()
        if status == "archived":
            emails = re.split(r"[;,]", row["contact_emails"])
            for email in emails:
                email = email.strip()
                if "noreply.gitlab.com" in email or email == "list@gmail.com":
                    continue
                clean_row = {
                    "book_id": row["book_id"].strip(),
                    "status": row["status"].strip(),
                    "contact_emails": email
                }
                writer.writerow(clean_row)
                # Print in CSV format
                print(f'{clean_row["book_id"]},{clean_row["status"]},{clean_row["contact_emails"]}')
                break  # only first valid author email

    infile.close()
    outfile.close()
    print(f"\n✅ Output also saved to: {output_file}")

# Run it
extract_author_emails()

```
