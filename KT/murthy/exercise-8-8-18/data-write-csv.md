
```

import csv

file = 'test.csv'
data = [
    ["name", "score"],
    ["virat", "100"],
    ["rohit", "120"]
]

f = open(file, newline='', mode='w')  # Using your original open syntax
w = csv.writer(f)

for row in data:
    w.writerow(row)

f.close()  # Don't forget to close the file

print(f"Data written to {file}")

```
