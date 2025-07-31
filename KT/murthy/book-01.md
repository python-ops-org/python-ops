
```

import csv

rows = [
    ["book_id", "authors", "price", "project_status", "contact_emails"],
    ["01", "tagore", 20, "archived", "tagore@gmail.com,rohan@gmail.com,bot_01@noreply.gitlab.com,list@gmail.com"],
    ["02", "hemingway", 25, "active", "ernest@gmail.com;sayan@gmail.com,bot_02@noreply.gitlab.com;list@gmail.com"],
    ["03", "austen", 18, "active", "jane@gmail.com,john@gmail.com,bot_03@noreply.gitlab.com,list.gitlabapacsupport@gmail.com"],
    ["04", "shakespeare", 22, "archived", "will@gmail.com,bob@gmail.com,bot_04@noreply.gitlab.com,list@gmail.com"],
    ["05", "orwell", 19, "active", "george@gmail.com,mike@gmail.com,bot_05@noreply.gitlab.com,gitlabapacsupport@gmail.com"],
    ["06", "rowling", 30, "active", "jk@gmail.com,sundar@gmail.com,bot_06@noreply.gitlab.com,list@gmail.com"],
    ["07", "tolkien", 28, "archived", "jrr@gmail.com,riya@gmail.com,bot_07@noreply.gitlab.com,list@gmail.com"],
    ["08", "dickens", 24, "active", "charles@gmail.com,rai@gmail.com,bot_08@noreply.gitlab.com,list@gmail.com"],
    ["09", "coelho", 21, "archived", "paulo@gmail.com,ravi@gmail.com,bot_09@noreply.gitlab.com,list@gmail.com"],
    ["10", "camus", 17, "active", "albert@gmail.com;surya@gmail.com,bot_10@noreply.gitlab.com,gitlabapacsupport@gmail.com"],
]

with open("input.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("✅ books_with_status.csv created.")



```
