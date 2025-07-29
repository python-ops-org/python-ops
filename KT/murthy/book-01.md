
```

import csv

rows = [
    ["book_id", "authors", "price", "status", "email_ids"],
    ["01", "tagore", 20, "archived", "tagore@gmail.com,bot_01@noreply.gitlab.com,list@gmail.com"],
    ["02", "hemingway", 25, "live", "ernest@gmail.com;bot_02@noreply.gitlab.com;list@gmail.com"],
    ["03", "austen", 18, "live", "jane@gmail.com,bot_03@noreply.gitlab.com,list@gmail.com"],
    ["04", "shakespeare", 22, "archived", "will@gmail.com,bot_04@noreply.gitlab.com,list@gmail.com"],
    ["05", "orwell", 19, "live", "george@gmail.com,bot_05@noreply.gitlab.com,list@gmail.com"],
    ["06", "rowling", 30, "live", "jk@gmail.com,bot_06@noreply.gitlab.com,list@gmail.com"],
    ["07", "tolkien", 28, "archived", "jrr@gmail.com,bot_07@noreply.gitlab.com,list@gmail.com"],
    ["08", "dickens", 24, "live", "charles@gmail.com,bot_08@noreply.gitlab.com,list@gmail.com"],
    ["09", "coelho", 21, "archived", "paulo@gmail.com,bot_09@noreply.gitlab.com,list@gmail.com"],
    ["10", "camus", 17, "live", "albert@gmail.com;bot_10@noreply.gitlab.com,list@gmail.com"],
]

with open("books_with_status.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("✅ books_with_status.csv created.")


```
