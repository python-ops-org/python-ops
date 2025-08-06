
```

import csv

input_file = "output2.csv"
output_file = "output_filtered.csv"

# Set to store already seen emails
seen_emails = set()

# List to collect output rows
output_rows = []

with open(input_file, newline='') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        cati = row['cati']
        project_id = row['project_id']
        raw_emails = row['contact_emails'].replace('"', '')
        split_emails = [email.strip() for email in raw_emails.replace(';', ',').split(',') if email.strip()]

        filtered_unique_emails = []
        for email in sorted(set(split_emails)):
            if (email.startswith('group_') and email.endswith('_bot@credit-suisse.com')) or \
               'noreply.gitlab.com' in email or \
               '.list' in email or \
               'list.gitlab' in email:
                continue
            if email not in seen_emails:
                seen_emails.add(email)
                filtered_unique_emails.append(email)

        if filtered_unique_emails:
            output_rows.append([cati, project_id] + filtered_unique_emails)
        else:
            output_rows.append([cati, project_id])

# Write to CSV
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['cati', 'project_id', 'contact_emails'])  # Header

    for row in output_rows:
        if len(row) > 2:
            # Re-join contact_emails in same column
            writer.writerow([row[0], row[1], ','.join(row[2:])])
        else:
            writer.writerow(row)

```
